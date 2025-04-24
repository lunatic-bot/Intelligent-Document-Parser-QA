from typing import Optional
import fitz  # PyMuPDF for PDFs
import docx  # python-docx for DOCX files

def parse_pdf(file_path: str) -> str:
    """
    Extract text from a text-based PDF using PyMuPDF.
    """
    text = []
    doc = fitz.open(file_path)
    for page in doc:
        text.append(page.get_text())
    doc.close()
    return "\n".join(text)

def parse_docx(file_path: str) -> str:
    """
    Extract text from a DOCX file using python-docx.
    """
    doc = docx.Document(file_path)
    text = [para.text for para in doc.paragraphs]
    return "\n".join(text)

def parse_txt(file_path: str, encoding: str = 'utf-8') -> str:
    """
    Read text from a plain TXT file.
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()

def parse_document(file_path: str, file_type: Optional[str] = None) -> str:
    """
    Dispatch to the correct parser based on file extension or provided file_type.
    Supported types: pdf, docx, txt
    """
    # Determine file type by extension if not provided
    if not file_type:
        file_type = file_path.split('.')[-1].lower()

    if file_type == 'pdf':
        return parse_pdf(file_path)
    elif file_type == 'docx':
        return parse_docx(file_path)
    elif file_type == 'txt':
        return parse_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

# Example usage
if __name__ == "__main__":
    for path in ["sample.pdf", "sample.docx", "sample.txt"]:
        try:
            content = parse_document(path)
            print(f"Extracted content from {path}:\n{content[:200]}...\n")
        except Exception as e:
            print(f"Failed to parse {path}: {e}")

