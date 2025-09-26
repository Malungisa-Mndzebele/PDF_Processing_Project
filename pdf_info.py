import fitz  # PyMuPDF
import sys

def analyze_pdf(file_path):
    try:
        # Open the PDF
        doc = fitz.open(file_path)
        
        print(f"PDF Analysis for: {file_path}")
        print("=" * 60)
        
        # Basic information
        print(f"Number of pages: {len(doc)}")
        print(f"PDF version: {doc.metadata.get('format', 'Unknown')}")
        print(f"Title: {doc.metadata.get('title', 'No title')}")
        print(f"Author: {doc.metadata.get('author', 'No author')}")
        print(f"Subject: {doc.metadata.get('subject', 'No subject')}")
        print(f"Creator: {doc.metadata.get('creator', 'No creator')}")
        print(f"Producer: {doc.metadata.get('producer', 'No producer')}")
        print(f"Creation date: {doc.metadata.get('creationDate', 'No creation date')}")
        print(f"Modification date: {doc.metadata.get('modDate', 'No modification date')}")
        
        print("\n" + "=" * 60)
        
        # Check if pages contain images
        total_images = 0
        pages_with_images = 0
        
        for page_num in range(min(10, len(doc))):  # Check first 10 pages
            page = doc[page_num]
            image_list = page.get_images()
            if image_list:
                pages_with_images += 1
                total_images += len(image_list)
                print(f"Page {page_num + 1}: {len(image_list)} image(s)")
        
        print(f"\nFirst 10 pages analysis:")
        print(f"Pages with images: {pages_with_images}")
        print(f"Total images found: {total_images}")
        
        # Check page dimensions
        if len(doc) > 0:
            first_page = doc[0]
            rect = first_page.rect
            print(f"\nPage dimensions: {rect.width} x {rect.height} points")
            print(f"Page dimensions: {rect.width/72:.2f} x {rect.height/72:.2f} inches")
        
        doc.close()
        
    except Exception as e:
        print(f"Error analyzing PDF: {e}")

if __name__ == "__main__":
    pdf_path = r"Request No. 1.pdf"
    analyze_pdf(pdf_path)
