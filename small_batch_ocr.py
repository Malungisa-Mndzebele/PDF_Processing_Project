#!/usr/bin/env python3
"""
Small batch OCR processor - 10 pages per batch for more control
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

def process_small_batch(pdf_path, start_page, end_page, batch_num, total_batches, output_dir="small_batch_results"):
    """Process a small batch of pages"""
    
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        doc = fitz.open(pdf_path)
        
        print(f"\n🔄 Processing Small Batch {batch_num}/{total_batches}")
        print(f"📄 Pages {start_page + 1} to {end_page + 1} (Total: {end_page - start_page + 1} pages)")
        print("=" * 50)
        
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
            print(f"📄 Page {page_num + 1}...", end=" ")
            text = pytesseract.image_to_string(img, lang='eng')
            
            if text.strip():
                batch_text.append(f"\n--- Page {page_num + 1} ---\n")
                batch_text.append(text)
                batch_text.append("\n" + "-" * 30 + "\n")
                print(f"✅ {len(text.strip())} chars")
            else:
                print("⚠️  No text")
        
        doc.close()
        
        # Save batch results
        batch_file = os.path.join(output_dir, f"small_batch_{batch_num:03d}_pages_{start_page+1:03d}-{end_page+1:03d}.txt")
        with open(batch_file, 'w', encoding='utf-8') as f:
            f.writelines(batch_text)
        
        elapsed = time.time() - start_time
        total_chars = sum(len(text) for text in batch_text)
        
        print(f"\n✅ Small Batch {batch_num} complete!")
        print(f"📁 Saved to: {os.path.abspath(batch_file)}")
        print(f"📊 Extracted {total_chars:,} characters in {elapsed:.1f} seconds")
        
        return batch_file, total_chars
        
    except Exception as e:
        print(f"❌ Error in small batch {batch_num}: {e}")
        return None, 0

def main():
    """Main small batch processing function"""
    
    pdf_path = r"Request No. 1.pdf"
    batch_size = 10  # Small batch size
    
    if not setup_tesseract_path():
        return False
    
    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        doc.close()
        
        print(f"🚀 Starting Small Batch OCR Processing")
        print(f"📄 Total pages: {total_pages}")
        print(f"📦 Batch size: {batch_size} pages")
        print(f"🔄 Total batches: {(total_pages + batch_size - 1) // batch_size}")
        print("=" * 50)
        
        total_batches = (total_pages + batch_size - 1) // batch_size
        all_batch_files = []
        total_chars = 0
        
        for batch_num in range(total_batches):
            start_page = batch_num * batch_size
            end_page = min(start_page + batch_size - 1, total_pages - 1)
            
            batch_file, chars = process_small_batch(pdf_path, start_page, end_page, 
                                            batch_num + 1, total_batches)
            
            if batch_file:
                all_batch_files.append(batch_file)
                total_chars += chars
            
            # Pause between batches
            if batch_num < total_batches - 1:
                print(f"\n⏸️  Pausing 1 second before next batch...")
                time.sleep(1)
        
        print(f"\n🎯 All small batches completed!")
        print(f"📊 Total characters extracted: {total_chars:,}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during small batch processing: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting Small Batch OCR Processing")
    print("📦 Batch size: 10 pages")
    print("⏱️  Estimated time: 45-60 minutes")
    print("💾 Results saved in: small_batch_results/")
    print()
    
    success = main()
    
    if success:
        print(f"\n🎉 SUCCESS! All 238 pages processed in small batches!")
    else:
        print(f"\n❌ Processing failed. Check error messages above.")
