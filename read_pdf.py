import PyPDF2
import sys

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            print(f"PDF has {len(pdf_reader.pages)} pages")
            print("=" * 50)
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                print(f"\n--- Page {page_num} ---")
                text = page.extract_text()
                print(text)
                print("-" * 30)
                
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    pdf_path = r"C:\Users\1\Downloads\Request No. 1.pdf"
    read_pdf(pdf_path)
