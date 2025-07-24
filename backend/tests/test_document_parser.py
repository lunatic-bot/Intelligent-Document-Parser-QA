import os
import pytest
from app.core.document_parser.dispatcher import DocumentParser
from app.core.document_parser.normalizer import TextNormalizer

# Dummy file paths (replace with real test data paths)
# PDF_PATH = "sample_files/sample.pdf"
# DOCX_PATH = "sample_files/sample.docx"
# TXT_PATH = "sample_files/sample.txt"
# IMG_PDF_PATH = "sample_files/sample_image.pdf"

BASE_DIR = os.path.dirname(__file__)
SAMPLE_DIR = os.path.join(BASE_DIR, "sample_files")

PDF_PATH = os.path.join(SAMPLE_DIR, "sample.pdf")
DOCX_PATH = os.path.join(SAMPLE_DIR, "sample.docx")
TXT_PATH = os.path.join(SAMPLE_DIR, "sample.txt")
IMG_PDF_PATH = os.path.join(SAMPLE_DIR, "sample_image.pdf")

@pytest.fixture(scope="module")
def parser():
    return DocumentParser(
        poppler_path=r"C:\Users\atalb\AppData\Local\poppler-24.08.0\Library\bin",
    tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

@pytest.mark.parametrize("file_path,file_type", [
    (PDF_PATH, "pdf"),
    (DOCX_PATH, "docx"),
    (TXT_PATH, "txt"),
    (IMG_PDF_PATH, "pdf")
])
def test_parse_document(parser, file_path, file_type):
    assert os.path.exists(file_path), f"Test file not found: {file_path}"
    raw_text = parser.parse(file_path, file_type)
    normalized = TextNormalizer.normalize(raw_text)
    assert isinstance(normalized, str)
    assert len(normalized) > 10  # crude check for non-empty output


