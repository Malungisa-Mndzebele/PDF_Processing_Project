#!/usr/bin/env python3
"""
Test script - process only first 20 pages to verify everything works
"""

import pytesseract
import os
import io
from PIL import Image
import fitz  # PyMuPDF
import time

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

def test_first_batch():
    """Test OCR on first 20 pages only"""
    
    pdf_path = r"Request No. 1.pdf"
    
    if not setup_tesseract_path():
        return False
    
    try:
        doc = fitz.open(pdf_path)
        
        print(f"🧪 Testing OCR on first 20 pages")
        print("=" * 40)
        
        all_text = []
        start_time = time.time()
        
        for page_num in range(min(20, len(doc))):
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
                all_text.append(f"\n--- Page {page_num + 1} ---\n")
                all_text.append(text)
                all_text.append("\n" + "-" * 30 + "\n")
                print(f"✅ {len(text.strip())} chars")
            else:
                print("⚠️  No text")
        
        doc.close()
        
        # Save test results
        with open("test_first_20_pages.txt", 'w', encoding='utf-8') as f:
            f.writelines(all_text)
        
        elapsed = time.time() - start_time
        total_chars = sum(len(text) for text in all_text)
        
        print(f"\n🎉 Test complete!")
        print(f"📁 Saved to: test_first_20_pages.txt")
        print(f"📊 Extracted {total_chars:,} characters in {elapsed:.1f} seconds")
        print(f"⚡ Speed: {elapsed/20:.1f}s per page")
        
        # Show preview
        if all_text:
            preview = ''.join(all_text[:500])
            print(f"\n📖 Preview:\n{preview}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing OCR on first 20 pages")
    print("⏱️  Estimated time: 2-3 minutes")
    print()
    
    success = test_first_batch()
    
    if success:
        print(f"\n✅ Test successful! Ready for full processing.")
        print(f"💡 Run 'python start_batch_ocr.py' for all 238 pages")
    else:
        print(f"\n❌ Test failed. Check error messages above.")
