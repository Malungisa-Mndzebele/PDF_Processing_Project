#!/usr/bin/env python3
"""
Combine all small batch OCR results into one comprehensive text file
"""

import os
from datetime import datetime

def combine_small_batch_results():
    """Combine all small batch results into one file"""
    
    input_dir = "small_batch_results"
    output_file = "extracted_text_complete.txt"
    
    if not os.path.exists(input_dir):
        print(f"❌ Input directory {input_dir} not found")
        return False
    
    # Get all batch files and sort them
    batch_files = [f for f in os.listdir(input_dir) if f.startswith("small_batch_") and f.endswith(".txt")]
    batch_files.sort()
    
    if not batch_files:
        print(f"❌ No batch files found in {input_dir}")
        return False
    
    print(f"🔗 Combining {len(batch_files)} small batch files...")
    print(f"📁 Input directory: {os.path.abspath(input_dir)}")
    print(f"📄 Output file: {os.path.abspath(output_file)}")
    print("=" * 60)
    
    all_text = []
    total_chars = 0
    total_pages = 0
    
    # Add comprehensive header
    all_text.append("PDF TEXT EXTRACTION RESULTS\n")
    all_text.append("=" * 80 + "\n")
    all_text.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    all_text.append(f"Source: Request No. 1.pdf (238 pages)\n")
    all_text.append(f"Method: Tesseract OCR v5.5.0\n")
    all_text.append(f"Processing: Small batch processing (10 pages per batch)\n")
    all_text.append(f"Total batches: {len(batch_files)}\n")
    all_text.append("=" * 80 + "\n\n")
    
    # Process each batch file
    for i, batch_file in enumerate(batch_files, 1):
        batch_path = os.path.join(input_dir, batch_file)
        print(f"📄 Processing {batch_file} ({i}/{len(batch_files)})...")
        
        try:
            with open(batch_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Count pages in this batch
                page_count = content.count("--- Page ")
                total_pages += page_count
                
                all_text.append(content)
                total_chars += len(content)
                
                print(f"   ✅ Added {page_count} pages, {len(content):,} characters")
                
        except Exception as e:
            print(f"   ❌ Error reading {batch_file}: {e}")
    
    # Add footer
    all_text.append("\n" + "=" * 80 + "\n")
    all_text.append("END OF DOCUMENT\n")
    all_text.append(f"Total pages processed: {total_pages}\n")
    all_text.append(f"Total characters extracted: {total_chars:,}\n")
    all_text.append(f"Average characters per page: {total_chars//total_pages if total_pages > 0 else 0:,}\n")
    all_text.append("=" * 80 + "\n")
    
    # Save combined results
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(all_text)
        
        print(f"\n🎉 All batches combined successfully!")
        print(f"📁 Final file: {os.path.abspath(output_file)}")
        print(f"📊 Total pages: {total_pages}")
        print(f"📊 Total characters: {total_chars:,}")
        print(f"📊 Average per page: {total_chars//total_pages if total_pages > 0 else 0:,} chars")
        print(f"📊 File size: {os.path.getsize(output_file):,} bytes")
        
        return True
        
    except Exception as e:
        print(f"❌ Error saving combined file: {e}")
        return False

if __name__ == "__main__":
    print("🔗 Combining Small Batch OCR Results")
    print("=" * 50)
    
    success = combine_small_batch_results()
    
    if success:
        print(f"\n✅ SUCCESS! All OCR results combined into 'extracted_text_complete.txt'")
    else:
        print(f"\n❌ Failed to combine results. Check error messages above.")
