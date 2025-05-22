from typing import Optional
from pdf_parse import parse_pdf
from docs import parse_docx
from ocr import ocr_pdf


from typing import Literal
import fitz  # PyMuPDF

def detect_pdf_type(file_path: str, text_threshold: int = 100) -> Literal['text', 'image', 'mixed']:
    """
    Detect whether a PDF is text-based, image-based, or mixed.
    
    :param file_path: Path to the PDF file.
    :param text_threshold: Minimum number of characters per page to consider it text-based.
    :return: 'text', 'image', or 'mixed'
    """
    doc = fitz.open(file_path)
    total_pages = doc.page_count
    text_pages = 0
    image_pages = 0
    
    for page in doc:
        text = page.get_text().strip()
        if len(text) >= text_threshold:
            text_pages += 1
        else:
            # Check if there are images on the page
            images = page.get_images(full=True)
            if images:
                image_pages += 1
            else:
                # Neither text nor image, consider as text page with low content
                text_pages += 1
    
    doc.close()
    
    if text_pages == total_pages:
        return 'text'
    if image_pages == total_pages:
        return 'image'
    return 'mixed'



def parse_document(file_path: str, file_type: Optional[str] = None) -> str:
    """
    Dispatch to the correct parser based on file extension or provided file_type.
    Supported types: pdf, docx, txt
    """
    # Determine file type by extension if not provided
    if not file_type:
        file_type = file_path.split('.')[-1].lower()

    if file_type == 'pdf':
        pdf_type = detect_pdf_type(file_path)
        print("file type and pdf type : ", file_type, pdf_type)
        if pdf_type == 'text':
            raw_text = parse_pdf(file_path)
        elif pdf_type == 'image':
            raw_text = ocr_pdf(file_path)
        print(raw_text)
        return parse_pdf(file_path)
    elif file_type == 'docx':
        return parse_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")




pdf_file_path = r"C:\Users\atalb\Documents\Coding\FastAPI\IDP\backend\app\Data\100KB_PDF.pdf"
# pdf_file_path = r"C:\Users\atalb\Documents\Coding\FastAPI\IDP\backend\app\Data\image-based-pdf-sample.pdf"


if __name__ == "__main__":
    # pdf_text_extraction(pdf_file_path=pdf_file_path)
    text = parse_document(pdf_file_path, file_type="pdf")
    print(text)