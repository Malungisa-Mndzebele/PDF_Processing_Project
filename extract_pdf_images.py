import fitz  # PyMuPDF
import os
from PIL import Image
import io

def extract_images_from_pdf(pdf_path, output_dir="pdf_images"):
    """
    Extract images from PDF pages and save them as individual image files.
    This allows you to use any OCR tool on the extracted images.
    """
    try:
        # Create output directory
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Open the PDF
        doc = fitz.open(pdf_path)
        
        print(f"Extracting images from PDF: {pdf_path}")
        print(f"PDF has {len(doc)} pages")
        print(f"Output directory: {output_dir}")
        print("=" * 60)
        
        total_images = 0
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Convert page to image
            mat = fitz.Matrix(2.0, 2.0)  # 2x zoom for better quality
            pix = page.get_pixmap(matrix=mat)
            
            # Save page as image
            page_image_path = os.path.join(output_dir, f"page_{page_num + 1:03d}.png")
            pix.save(page_image_path)
            
            # Also check for embedded images in the page
            image_list = page.get_images()
            if image_list:
                print(f"Page {page_num + 1}: Found {len(image_list)} embedded image(s)")
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)
                    if pix.n - pix.alpha < 4:  # GRAY or RGB
                        img_path = os.path.join(output_dir, f"page_{page_num + 1:03d}_img_{img_index + 1}.png")
                        pix.save(img_path)
                        total_images += 1
                    pix = None
            
            if (page_num + 1) % 10 == 0:
                print(f"Processed {page_num + 1} pages...")
        
        doc.close()
        
        print(f"\nExtraction complete!")
        print(f"Total embedded images extracted: {total_images}")
        print(f"Page images saved: {len(doc)} pages")
        print(f"All images saved in: {os.path.abspath(output_dir)}")
        
        return output_dir
        
    except Exception as e:
        print(f"Error extracting images: {e}")
        return None

def create_ocr_instructions(output_dir):
    """Create instructions for using OCR on the extracted images"""
    instructions = f"""
OCR Instructions for PDF Text Extraction
========================================

The PDF has been converted to images and saved in: {os.path.abspath(output_dir)}

To extract text from these images, you can:

1. ONLINE OCR SERVICES:
   - Google Drive: Upload images to Google Drive, right-click > "Open with Google Docs"
   - Adobe Acrobat Online: https://www.adobe.com/acrobat/online/pdf-to-word.html
   - OnlineOCR.net: https://www.onlineocr.net/
   - SmallPDF: https://smallpdf.com/pdf-to-word

2. INSTALL TESSERACT OCR (for local processing):
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install the Windows version
   - Then run: python ocr_extract.py

3. MICROSOFT OFFICE:
   - Open images in Microsoft Word
   - Use "Insert > Pictures" then right-click > "Copy Text from Picture"

4. GOOGLE LENS (mobile):
   - Take photos of the images with Google Lens app
   - Use "Text" mode to extract text

The images are numbered sequentially (page_001.png, page_002.png, etc.)
Start with the first few pages to test the OCR quality.
"""
    
    with open(os.path.join(output_dir, "OCR_INSTRUCTIONS.txt"), "w", encoding="utf-8") as f:
        f.write(instructions)
    
    print(instructions)

if __name__ == "__main__":
    pdf_path = r"C:\Users\1\Downloads\Request No. 1.pdf"
    output_dir = extract_images_from_pdf(pdf_path)
    
    if output_dir:
        create_ocr_instructions(output_dir)
