import fitz  # PyMuPDF
import sys

def read_pdf_with_fitz(file_path):
    try:
        # Open the PDF
        doc = fitz.open(file_path)
        
        print(f"PDF has {len(doc)} pages")
        print("=" * 50)
        
        # Read first few pages to see if there's content
        for page_num in range(min(5, len(doc))):  # Read first 5 pages
            page = doc[page_num]
            text = page.get_text()
            
            print(f"\n--- Page {page_num + 1} ---")
            if text.strip():
                print(text)
            else:
                print("(No text content found on this page)")
            print("-" * 30)
            
        # Check if there are any pages with content
        pages_with_content = 0
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            if text.strip():
                pages_with_content += 1
                
        print(f"\nSummary: {pages_with_content} out of {len(doc)} pages contain text content")
        
        doc.close()
        
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    pdf_path = r"Request No. 1.pdf"
    read_pdf_with_fitz(pdf_path)
