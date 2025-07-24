class DOCXParser:
    def parse(self, file_path):
        import docx
        doc = docx.Document(file_path)
        return "\n".join(para.text for para in doc.paragraphs)
