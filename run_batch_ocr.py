#!/usr/bin/env python3
"""
Quick launcher for batch OCR processing
"""

import os
import sys

def main():
    print("🚀 PDF Batch OCR Processor")
    print("=" * 40)
    print("📄 Processing: Request No. 1.pdf (238 pages)")
    print("🔧 Tesseract OCR v5.5.0")
    print()
    
    # Check if PDF exists
    pdf_path = "Request No. 1.pdf"
    if not os.path.exists(pdf_path):
        print(f"❌ PDF file not found: {pdf_path}")
        return
    
    # Batch size options
    print("📦 Choose batch size:")
    print("1. Small batches (10 pages) - More control, slower")
    print("2. Medium batches (20 pages) - Balanced (recommended)")
    print("3. Large batches (30 pages) - Faster, less control")
    print("4. Custom batch size")
    print()
    
    try:
        choice = input("Enter choice (1-4, default 2): ").strip() or "2"
        
        if choice == "1":
            batch_size = 10
        elif choice == "2":
            batch_size = 20
        elif choice == "3":
            batch_size = 30
        elif choice == "4":
            batch_size = int(input("Enter custom batch size (5-50): "))
        else:
            batch_size = 20
        
        if batch_size < 5 or batch_size > 50:
            print("⚠️  Batch size adjusted to 20 (recommended range: 5-50)")
            batch_size = 20
            
    except ValueError:
        batch_size = 20
    
    print(f"\n✅ Batch size set to: {batch_size} pages")
    print(f"🔄 Total batches: {(238 + batch_size - 1) // batch_size}")
    print(f"⏱️  Estimated time: {((238 + batch_size - 1) // batch_size) * 2:.0f}-{((238 + batch_size - 1) // batch_size) * 3:.0f} minutes")
    print()
    
    # Confirm before starting
    confirm = input("🚀 Start batch processing? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("❌ Processing cancelled.")
        return
    
    print(f"\n🚀 Starting batch OCR processing...")
    print("💡 You can monitor progress in the terminal")
    print("📁 Results will be saved in 'batch_results/' folder")
    print("🔗 Final combined file: 'extracted_text_complete.txt'")
    print()
    
    # Import and run the batch processor
    try:
        from batch_ocr_extract import batch_ocr_extract
        success = batch_ocr_extract(pdf_path, batch_size)
        
        if success:
            print(f"\n🎉 SUCCESS! All 238 pages processed!")
            print(f"📁 Check 'extracted_text_complete.txt' for the final result")
        else:
            print(f"\n❌ Processing failed. Check error messages above.")
            
    except ImportError as e:
        print(f"❌ Error importing batch processor: {e}")
        print("Make sure 'batch_ocr_extract.py' is in the same directory")

if __name__ == "__main__":
    main()
