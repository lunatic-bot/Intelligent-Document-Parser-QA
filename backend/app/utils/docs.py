  # parse_docx(file_path) -> str

import docx

def parse_docx(file_path: str) -> str:
    """
    Extract text from a DOCX file using python-docx.
    """
    doc = docx.Document(file_path)
    text = [para.text for para in doc.paragraphs]
    return "\n".join(text)