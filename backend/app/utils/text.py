 # normalize_text(text) -> str
import re

def normalize_text(text: str) -> str:
    # Strip leading/trailing whitespace on each line
    lines = [line.strip() for line in text.splitlines()]
    text = " ".join(lines)
    # Collapse multiple spaces/newlines into one space
    text = re.sub(r'\s+', ' ', text)
    # Optionally lowercase
    text = text.lower()
    return text.strip()