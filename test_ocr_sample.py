import pytesseract
import os
import io
from PIL import Image
import fitz  # PyMuPDF

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

def test_ocr_on_sample_pages(pdf_path, num_pages=5, output_file="sample_extracted_text.txt"):
    """Test OCR on first few pages only"""
    if not setup_tesseract_path():
        return False
    
    try:
        doc = fitz.open(pdf_path)
        
        print(f"🧪 Testing OCR on first {num_pages} pages of: {pdf_path}")
        print("=" * 60)
        
        all_text = []
        
        for page_num in range(min(num_pages, len(doc))):
            page = doc[page_num]
            
            # Convert page to image
            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for better OCR quality
            pix = page.get_pixmap(matrix=mat)
            
            # Convert to PIL Image
            img_data = pix.tobytes("png")
            img = Image.open(io.BytesIO(img_data))
            
            # Extract text using OCR
            print(f"📄 Processing page {page_num + 1}...")
            text = pytesseract.image_to_string(img, lang='eng')
            
            if text.strip():
                all_text.append(f"\n--- Page {page_num + 1} ---\n")
                all_text.append(text)
                all_text.append("\n" + "-" * 50 + "\n")
                print(f"✅ Extracted {len(text.strip())} characters from page {page_num + 1}")
            else:
                print(f"⚠️  No text found on page {page_num + 1}")
        
        doc.close()
        
        # Save extracted text
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(all_text)
        
        print(f"\n🎉 Sample OCR test complete!")
        print(f"📁 Sample text saved to: {os.path.abspath(output_file)}")
        
        # Show preview of extracted text
        if all_text:
            preview = ''.join(all_text[:1000])  # First 1000 characters
            print(f"\n📖 Preview of extracted text:\n{preview}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during OCR test: {e}")
        return False

if __name__ == "__main__":
    pdf_path = r"Request No. 1.pdf"
    success = test_ocr_on_sample_pages(pdf_path, num_pages=5)
    
    if success:
        print(f"\n💡 If the sample looks good, run 'python ocr_extract.py' for all 238 pages!")
    else:
        print(f"\n❌ OCR test failed. Check the error messages above.")
