# 📸 PDF Processing Project - Complete Image Collection

A comprehensive web application for viewing and browsing all 476 images extracted from PDF documents related to Jeffrey Epstein's birthday book collection, featuring an interactive image gallery with advanced filtering and search capabilities.

## 📚 Source Information

**Document Source:** This collection contains images extracted from PDF documents related to Jeffrey Epstein's birthday book collection.

**Original Documents:** [Google Drive Folder - Request Documents](https://drive.google.com/drive/folders/1ZSVpXEhI7gKI0zatJdYe6QhKJ5pjUo4b)

**Background Information:** [PBS NewsHour - Epstein Birthday Book Coverage](https://www.pbs.org/newshour/nation/see-epsteins-full-birthday-book-with-alleged-personal-messages-from-trump-clinton-and-others)

**Note:** These documents were released by the House Oversight Committee and are part of the public record.

## 🎯 Project Overview

This project processes a PDF document and creates an interactive web interface to view all extracted images. The website displays:
- **238 Page Images** - Full page scans from the PDF
- **238 Embedded Images** - Photos and graphics found within the document
- **Total: 476 Images** - Complete collection in one place

## 🚀 Features

### 📸 Image Gallery
- **Complete Image Collection** - All 476 images from the PDF
- **Interactive Grid Layout** - Responsive design for all screen sizes
- **Full-Size Modal Viewing** - Click any image to view in full resolution
- **Lazy Loading** - Optimized performance for large image collections

### 🔍 Advanced Filtering
- **All Images** - View the complete collection
- **Page Images Only** - Filter to show only full page scans
- **Embedded Images Only** - Filter to show only embedded photos/graphics
- **Time-Based Filtering** - Early (1-50), Middle (51-150), Late (151-238) pages

### 🔎 Search Functionality
- **Real-Time Search** - Instant filtering as you type
- **Page Number Search** - Find specific pages quickly
- **Title & Description Search** - Search through image metadata

### 🎨 Visual Design
- **Modern UI** - Clean, colorful interface with gradients
- **Animated Elements** - Smooth transitions and hover effects
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Comic Book Style** - Fun, playful design with Comic Sans MS font

## 📁 Project Structure

```
PDF_Processing_Project/
├── index.html              # Main website file
├── pdf_images/             # All extracted images (476 files)
│   ├── page_001.png        # Page images (1-238)
│   ├── page_001_img_1.png  # Embedded images (1-238)
│   └── ...
├── *.py                    # Python processing scripts
├── small_batch_results/    # OCR text extraction results
├── extracted_text_complete.txt  # Combined OCR text
├── content_analysis.json   # Content analysis results
└── README.md              # This file
```

## 🛠️ Python Scripts

### Core Processing Scripts
- **`pdf_info.py`** - Basic PDF information and metadata analysis
- **`extract_pdf_images.py`** - Extract all images from PDF to PNG files
- **`ocr_extract.py`** - OCR text extraction using Tesseract
- **`read_pdf_fitz.py`** - Direct text extraction using PyMuPDF
- **`read_pdf.py`** - Alternative text extraction using PyPDF2

### Batch Processing Scripts
- **`batch_ocr_extract.py`** - Process PDF in batches for OCR
- **`start_batch_ocr.py`** - Non-interactive batch processing
- **`small_batch_ocr.py`** - Small batch processing (10 pages)
- **`test_first_batch.py`** - Test processing (first 20 pages)
- **`combine_ocr_results.py`** - Combine all batch results

### Analysis Scripts
- **`analyze_content.py`** - Content analysis and categorization
- **`online_ocr_guide.py`** - Guide for online OCR services

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Tesseract OCR (for text extraction)
- Modern web browser

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd PDF_Processing_Project
   ```

2. Install Python dependencies:
   ```bash
   pip install PyMuPDF pytesseract Pillow PyPDF2
   ```

3. Install Tesseract OCR:
   - Windows: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - macOS: `brew install tesseract`
   - Linux: `sudo apt-get install tesseract-ocr`

### Usage

#### View the Image Collection
1. Open `index.html` in your web browser
2. Browse through all 476 images
3. Use filters to view specific image types
4. Search for specific pages
5. Click images to view full-size

#### Process PDF Documents
1. Place your PDF file in the project directory
2. Update the file path in the Python scripts
3. Run the processing scripts:
   ```bash
   python pdf_info.py          # Get PDF information
   python extract_pdf_images.py # Extract all images
   python ocr_extract.py       # Extract text with OCR
   ```

## 📊 Technical Details

### Image Processing
- **Format**: PNG images extracted from PDF
- **Resolution**: High-quality extraction preserving original quality
- **Organization**: Systematic naming convention (page_XXX.png, page_XXX_img_1.png)

### Web Technologies
- **HTML5** - Semantic markup and structure
- **CSS3** - Modern styling with gradients and animations
- **JavaScript** - Interactive functionality and dynamic content
- **Responsive Design** - Mobile-first approach

### Performance Optimizations
- **Lazy Loading** - Images load as needed
- **Error Handling** - Graceful handling of missing images
- **Efficient Filtering** - Client-side filtering for fast response
- **Modal Viewing** - Full-size images without page reload

## 🎨 Design Features

### Visual Elements
- **Gradient Backgrounds** - Colorful, modern appearance
- **Animated Statistics** - Pulsing numbers and counters
- **Hover Effects** - Interactive feedback on all elements
- **Card-Based Layout** - Clean, organized image presentation

### User Experience
- **Intuitive Navigation** - Easy-to-use filter buttons
- **Real-Time Search** - Instant results as you type
- **Keyboard Support** - ESC key to close modals
- **Mobile Responsive** - Works on all device sizes

## 📈 Statistics

- **Total Images**: 476
- **Page Images**: 238
- **Embedded Images**: 238
- **File Size**: Optimized for web viewing
- **Loading Time**: Lazy loading for fast initial load

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Tesseract OCR** - For text extraction capabilities
- **PyMuPDF** - For PDF processing and image extraction
- **Modern Web Standards** - For responsive design and interactivity

## 📞 Support

If you encounter any issues or have questions:
1. Check the existing issues in the repository
2. Create a new issue with detailed information
3. Include system information and error messages

---

**Note**: This project processes PDF documents and extracts images for educational and research purposes. Please ensure you have appropriate permissions for any documents you process.
