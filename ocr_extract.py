import pytesseract
import os
import io
from PIL import Image
import fitz  # PyMuPDF

def setup_tesseract_path():
    """
    Try to find Tesseract installation on Windows
    """
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
    
    print("❌ Tesseract not found. Please install it from: https://github.com/UB-Mannheim/tesseract/wiki")
    return False

def extract_text_from_pdf_with_ocr(pdf_path, output_file="extracted_text.txt"):
    """
    Extract text from PDF using OCR
    """
    if not setup_tesseract_path():
        return False
    
    try:
        # Open the PDF
        doc = fitz.open(pdf_path)
        
        print(f"Extracting text from PDF using OCR: {pdf_path}")
        print(f"PDF has {len(doc)} pages")
        print("=" * 60)
        
        all_text = []
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Convert page to image
            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for better OCR quality
            pix = page.get_pixmap(matrix=mat)
            
            # Convert to PIL Image
            img_data = pix.tobytes("png")
            img = Image.open(io.BytesIO(img_data))
            
            # Extract text using OCR
            print(f"Processing page {page_num + 1}...")
            text = pytesseract.image_to_string(img, lang='eng')
            
            if text.strip():
                all_text.append(f"\n--- Page {page_num + 1} ---\n")
                all_text.append(text)
                all_text.append("\n" + "-" * 50 + "\n")
            
            if (page_num + 1) % 10 == 0:
                print(f"Completed {page_num + 1} pages...")
        
        doc.close()
        
        # Save extracted text
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(all_text)
        
        print(f"\nText extraction complete!")
        print(f"Extracted text saved to: {os.path.abspath(output_file)}")
        
        # Show preview of extracted text
        if all_text:
            preview = ''.join(all_text[:2000])  # First 2000 characters
            print(f"\nPreview of extracted text:\n{preview}...")
        
        return True
        
    except Exception as e:
        print(f"Error during OCR extraction: {e}")
        return False

if __name__ == "__main__":
    pdf_path = r"Request No. 1.pdf"
    success = extract_text_from_pdf_with_ocr(pdf_path)
    
    if not success:
        print("\nAlternative: Run 'python extract_pdf_images.py' to extract images for manual OCR processing.")
