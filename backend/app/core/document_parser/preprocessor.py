import re
from nltk.tokenize import sent_tokenize

class Preprocessor:
    def __init__(self, min_sentence_len: int = 5):
        self.min_len = min_sentence_len

    def clean_text(self, text: str) -> str:
        # Remove extra whitespace and non-printable characters
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[\x00-\x1F\x7F]+", "", text)
        return text.strip()

    def filter_sentences(self, text: str) -> str:
        sentences = sent_tokenize(text)
        filtered = [s for s in sentences if len(s.strip()) >= self.min_len]
        return " ".join(filtered)

    def process(self, text: str) -> str:
        cleaned = self.clean_text(text)
        return self.filter_sentences(cleaned)