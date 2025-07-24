class TextNormalizer:
    @staticmethod
    def normalize(text: str) -> str:
        import re
        lines = [line.strip() for line in text.splitlines()]
        text = " ".join(lines)
        text = re.sub(r'\s+', ' ', text)
        return text.lower().strip()