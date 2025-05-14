 # parse_pdf(file_path) -> str
import fitz

def parse_pdf(file_path: str) -> str:
    """
    Extract text from a text-based PDF using PyMuPDF.
    :param file_path: Path to the PDF file.
    :return: Extracted text as a single string.
    """
    text = []
    try:
        # Open the document
        doc = fitz.open(file_path)
        for page in doc:
            text.append(page.get_text())
        doc.close()
    except Exception as e:
        raise RuntimeError(f"Error parsing PDF: {e}")
    
    return "\n".join(text)