#!/usr/bin/env python3
"""
Non-interactive batch OCR processor - starts immediately with default settings
"""

import pytesseract
import os
import io
from PIL import Image
import fitz  # PyMuPDF
import time
from datetime import datetime

def setup_tesseract_path():
    """Setup Tesseract path"""
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        r"C:\Users\{}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe".format(os.getenv('USERNAME')),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            print(f"✅ Found Tesseract at: {path}")
            return True
    
    print("❌ Tesseract not found.")
    return False

def process_batch(pdf_path, start_page, end_page, batch_num, total_batches, output_dir="batch_results"):
    """Process a batch of pages"""
    
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        doc = fitz.open(pdf_path)
        
        print(f"\n🔄 Processing Batch {batch_num}/{total_batches}")
        print(f"📄 Pages {start_page + 1} to {end_page + 1} (Total: {end_page - start_page + 1} pages)")
        print("=" * 60)
        
        batch_text = []
        start_time = time.time()
        
        for page_num in range(start_page, min(end_page + 1, len(doc))):
            page = doc[page_num]
            
            # Convert page to image
            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for better OCR quality
            pix = page.get_pixmap(matrix=mat)
            
            # Convert to PIL Image
            img_data = pix.tobytes("png")
            img = Image.open(io.BytesIO(img_data))
            
            # Extract text using OCR
            print(f"📄 Processing page {page_num + 1}...", end=" ")
            text = pytesseract.image_to_string(img, lang='eng')
            
            if text.strip():
                batch_text.append(f"\n--- Page {page_num + 1} ---\n")
                batch_text.append(text)
                batch_text.append("\n" + "-" * 50 + "\n")
                print(f"✅ {len(text.strip())} chars")
            else:
                print("⚠️  No text")
            
            # Progress indicator
            if (page_num - start_page + 1) % 5 == 0:
                elapsed = time.time() - start_time
                pages_done = page_num - start_page + 1
                pages_remaining = end_page - page_num
                eta = (elapsed / pages_done) * pages_remaining
                print(f"   ⏱️  {pages_done} pages done, ~{eta:.0f}s remaining")
        
        doc.close()
        
        # Save batch results
        batch_file = os.path.join(output_dir, f"batch_{batch_num:03d}_pages_{start_page+1:03d}-{end_page+1:03d}.txt")
        with open(batch_file, 'w', encoding='utf-8') as f:
            f.writelines(batch_text)
        
        elapsed = time.time() - start_time
        total_chars = sum(len(text) for text in batch_text)
        
        print(f"\n✅ Batch {batch_num} complete!")
        print(f"📁 Saved to: {os.path.abspath(batch_file)}")
        print(f"📊 Extracted {total_chars:,} characters in {elapsed:.1f} seconds")
        print(f"⚡ Speed: {elapsed/(end_page-start_page+1):.1f}s per page")
        
        return batch_file, total_chars
        
    except Exception as e:
        print(f"❌ Error in batch {batch_num}: {e}")
        return None, 0

def combine_batch_results(output_dir="batch_results", final_file="extracted_text_complete.txt"):
    """Combine all batch results into one file"""
    
    if not os.path.exists(output_dir):
        print(f"❌ Output directory {output_dir} not found")
        return False
    
    batch_files = [f for f in os.listdir(output_dir) if f.startswith("batch_") and f.endswith(".txt")]
    batch_files.sort()
    
    if not batch_files:
        print(f"❌ No batch files found in {output_dir}")
        return False
    
    print(f"\n🔗 Combining {len(batch_files)} batch files...")
    
    all_text = []
    total_chars = 0
    
    # Add header
    all_text.append(f"PDF Text Extraction Results\n")
    all_text.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    all_text.append(f"Source: Request No. 1.pdf (238 pages)\n")
    all_text.append(f"Method: Tesseract OCR v5.5.0\n")
    all_text.append("=" * 80 + "\n\n")
    
    for batch_file in batch_files:
        batch_path = os.path.join(output_dir, batch_file)
        print(f"📄 Adding {batch_file}...")
        
        with open(batch_path, 'r', encoding='utf-8') as f:
            content = f.read()
            all_text.append(content)
            total_chars += len(content)
    
    # Save combined results
    with open(final_file, 'w', encoding='utf-8') as f:
        f.writelines(all_text)
    
    print(f"\n🎉 All batches combined!")
    print(f"📁 Final file: {os.path.abspath(final_file)}")
    print(f"📊 Total characters: {total_chars:,}")
    print(f"📄 Total pages processed: 238")
    
    return True

def main():
    """Main batch processing function"""
    
    pdf_path = r"Request No. 1.pdf"
    batch_size = 20  # Default batch size
    
    if not setup_tesseract_path():
        return False
    
    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        doc.close()
        
        print(f"🚀 Starting Batch OCR Processing")
        print(f"📄 Total pages: {total_pages}")
        print(f"📦 Batch size: {batch_size} pages")
        print(f"🔄 Total batches: {(total_pages + batch_size - 1) // batch_size}")
        print("=" * 60)
        
        total_batches = (total_pages + batch_size - 1) // batch_size
        all_batch_files = []
        total_chars = 0
        
        for batch_num in range(total_batches):
            start_page = batch_num * batch_size
            end_page = min(start_page + batch_size - 1, total_pages - 1)
            
            batch_file, chars = process_batch(pdf_path, start_page, end_page, 
                                            batch_num + 1, total_batches)
            
            if batch_file:
                all_batch_files.append(batch_file)
                total_chars += chars
            
            # Pause between batches to prevent overheating
            if batch_num < total_batches - 1:
                print(f"\n⏸️  Pausing 2 seconds before next batch...")
                time.sleep(2)
        
        print(f"\n🎯 All batches completed!")
        print(f"📊 Total characters extracted: {total_chars:,}")
        
        # Combine results
        if all_batch_files:
            combine_batch_results()
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error during batch processing: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting Batch OCR Processing (Non-Interactive)")
    print("📦 Batch size: 20 pages")
    print("⏱️  Estimated time: 30-45 minutes")
    print("💾 Results saved in: batch_results/")
    print("🔗 Final file: extracted_text_complete.txt")
    print()
    
    success = main()
    
    if success:
        print(f"\n🎉 SUCCESS! All 238 pages processed!")
        print(f"📁 Check 'extracted_text_complete.txt' for the final result")
    else:
        print(f"\n❌ Processing failed. Check error messages above.")
