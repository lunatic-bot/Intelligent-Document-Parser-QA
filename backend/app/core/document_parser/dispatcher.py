from .pdf_parser import PDFParser
from .docx_parser import DOCXParser
from .txt_parser import TXTParser

class DocumentParser:
    def __init__(self, poppler_path=None, tesseract_cmd=None):
        self.pdf_parser = PDFParser(poppler_path, tesseract_cmd)
        self.docx_parser = DOCXParser()
        self.txt_parser = TXTParser()

    def parse(self, file_path, file_type=None):
        if not file_type:
            file_type = file_path.split('.')[-1].lower()

        if file_type == 'pdf':
            return self.pdf_parser.parse(file_path)
        elif file_type == 'docx':
            return self.docx_parser.parse(file_path)
        elif file_type == 'txt':
            return self.txt_parser.parse(file_path)
        raise ValueError(f"Unsupported file type: {file_type}")