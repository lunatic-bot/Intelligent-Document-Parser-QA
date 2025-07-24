class PDFParser:
    def __init__(self, poppler_path=None, tesseract_cmd=None):
        import pytesseract
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        self.poppler_path = poppler_path
        self.pytesseract = pytesseract

    def parse(self, file_path):
        pdf_type = self.detect_pdf_type(file_path)
        if pdf_type == 'text':
            return self._parse_text_pdf(file_path)
        elif pdf_type == 'image':
            return self._ocr_pdf(file_path)
        else:
            return self._parse_text_pdf(file_path) + "\n" + self._ocr_pdf(file_path)

    def _parse_text_pdf(self, file_path):
        import fitz
        text = []
        doc = fitz.open(file_path)
        for page in doc:
            text.append(page.get_text())
        doc.close()
        return "\n".join(text)

    def _ocr_pdf(self, file_path, dpi=300, temp_folder="temp_images"):
        import os
        from pdf2image import convert_from_path

        temp_folder = os.path.join(os.getcwd(), temp_folder)
        os.makedirs(temp_folder, exist_ok=True)

        images = convert_from_path(file_path, dpi=dpi, output_folder=temp_folder, fmt='png', poppler_path=self.poppler_path)
        text_pages = [self.pytesseract.image_to_string(image) for image in images]
        return "\n".join(text_pages)

    def detect_pdf_type(self, file_path, text_threshold=100):
        import fitz
        doc = fitz.open(file_path)
        total_pages = doc.page_count
        text_pages = image_pages = 0

        for page in doc:
            text = page.get_text().strip()
            if len(text) >= text_threshold:
                text_pages += 1
            elif page.get_images(full=True):
                image_pages += 1
            else:
                text_pages += 1
        doc.close()

        if text_pages == total_pages:
            return 'text'
        if image_pages == total_pages:
            return 'image'
        return 'mixed'
