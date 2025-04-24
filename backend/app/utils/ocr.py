# perform_ocr(image_path) -> str

from typing import List
from pdf2image import convert_from_path
import pytesseract
import os

def ocr_pdf(file_path: str, dpi: int = 300, temp_folder: str = "/tmp") -> str:
    """
    Perform OCR on an image-based PDF by converting each page to an image
    and extracting text via pytesseract.
    
    :param file_path: Path to the PDF file.
    :param dpi: Resolution for conversion.
    :param temp_folder: Folder to store temporary images.
    :return: Extracted text from all pages.
    """
    # Convert PDF pages to images
    images = convert_from_path(file_path, dpi=dpi, output_folder=temp_folder, fmt='png')
    
    # Perform OCR on each image
    text_pages: List[str] = []
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        text_pages.append(text)
        
        # Optionally remove the image file if saved
        if hasattr(image, 'filename') and os.path.exists(image.filename):
            os.remove(image.filename)
    
    return "\n".join(text_pages)