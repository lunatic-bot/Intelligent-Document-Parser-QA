# main.py
import os
from .dispatcher import DocumentParser
from .normalizer import TextNormalizer

# Test files directory
test_files = {
    "pdf": "tests/sample.pdf",
    "docx": "tests/sample.docx",
    "txt": "tests/sample.txt"
}

# Initialize parser with optional poppler/tesseract paths
parser = DocumentParser(
    poppler_path=r"C:\\Path\\To\\poppler\\bin",
    tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)

# Process each file
def process_file(file_type: str, file_path: str):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"\n=== Parsing {file_type.upper()} File ===")
    raw_text = parser.parse(file_path, file_type)
    normalized = TextNormalizer.normalize(raw_text)
    print(normalized[:500], "...\n")  # Preview first 500 chars


if __name__ == "__main__":
    for ftype, path in test_files.items():
        process_file(ftype, path)
