import os
import webbrowser
from pathlib import Path

def create_online_ocr_guide():
    """
    Create a guide for using online OCR services with the extracted images
    """
    
    pdf_images_dir = "pdf_images"
    
    if not os.path.exists(pdf_images_dir):
        print("❌ pdf_images directory not found. Run 'python extract_pdf_images.py' first.")
        return
    
    # Count images
    page_images = [f for f in os.listdir(pdf_images_dir) if f.startswith("page_") and f.endswith(".png") and "_img_" not in f]
    embedded_images = [f for f in os.listdir(pdf_images_dir) if f.startswith("page_") and "_img_" in f and f.endswith(".png")]
    
    print("🔍 PDF OCR Analysis & Online Processing Guide")
    print("=" * 60)
    print(f"📄 Total page images: {len(page_images)}")
    print(f"🖼️  Total embedded images: {len(embedded_images)}")
    print(f"📁 Images location: {os.path.abspath(pdf_images_dir)}")
    print()
    
    print("🌐 ONLINE OCR OPTIONS (No Installation Required):")
    print("-" * 50)
    
    print("\n1️⃣ GOOGLE DRIVE (Recommended - Free & Accurate)")
    print("   • Go to: https://drive.google.com")
    print("   • Upload images from pdf_images/ folder")
    print("   • Right-click image → 'Open with' → 'Google Docs'")
    print("   • Google automatically extracts text!")
    print("   • Copy text and save to .txt file")
    
    print("\n2️⃣ ADOBE ACROBAT ONLINE")
    print("   • Go to: https://www.adobe.com/acrobat/online/pdf-to-word.html")
    print("   • Upload your original PDF: 'Request No. 1.pdf'")
    print("   • Download converted Word document")
    print("   • Copy text to .txt file")
    
    print("\n3️⃣ ONLINEOCR.NET")
    print("   • Go to: https://www.onlineocr.net/")
    print("   • Upload images (free for small files)")
    print("   • Download extracted text")
    
    print("\n4️⃣ SMALLPDF")
    print("   • Go to: https://smallpdf.com/pdf-to-word")
    print("   • Upload PDF and convert to Word")
    print("   • Extract text from Word document")
    
    print("\n📱 MOBILE OPTIONS:")
    print("-" * 20)
    print("• Google Lens app - take photos of images")
    print("• Microsoft Office Lens - scan and extract text")
    print("• Adobe Scan - mobile OCR app")
    
    print("\n💡 RECOMMENDED WORKFLOW:")
    print("-" * 30)
    print("1. Start with Google Drive method (easiest)")
    print("2. Process first 5-10 pages to test quality")
    print("3. If quality is good, continue with more pages")
    print("4. Combine all extracted text into one document")
    
    print(f"\n📂 SAMPLE IMAGES TO TEST:")
    print("-" * 30)
    if page_images:
        sample_images = sorted(page_images)[:5]
        for img in sample_images:
            print(f"   • {img}")
    
    print(f"\n🎯 QUICK START:")
    print("-" * 15)
    print("1. Open Google Drive in your browser")
    print("2. Upload these sample images:")
    if page_images:
        for img in sample_images[:3]:
            print(f"   - {pdf_images_dir}/{img}")
    print("3. Right-click each image → 'Open with Google Docs'")
    print("4. Copy the extracted text")
    print("5. Save as 'extracted_text_sample.txt'")
    
    # Create a batch file for easy access
    create_batch_commands()
    
    return True

def create_batch_commands():
    """Create helpful batch commands"""
    
    commands = """@echo off
echo PDF OCR Processing Commands
echo ==========================

echo.
echo 1. Open Google Drive:
start https://drive.google.com

echo.
echo 2. Open Adobe Acrobat Online:
start https://www.adobe.com/acrobat/online/pdf-to-word.html

echo.
echo 3. Open OnlineOCR:
start https://www.onlineocr.net/

echo.
echo 4. Open SmallPDF:
start https://smallpdf.com/pdf-to-word

echo.
echo 5. Open PDF Images Folder:
explorer pdf_images

echo.
echo All OCR services opened! Choose your preferred method.
pause
"""
    
    with open("open_ocr_services.bat", "w") as f:
        f.write(commands)
    
    print(f"\n✅ Created 'open_ocr_services.bat' - double-click to open all OCR services!")

if __name__ == "__main__":
    create_online_ocr_guide()
