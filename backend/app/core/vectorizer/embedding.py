# core/vectorizer/embedding.py
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List

class EmbeddingService:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]) -> List[np.ndarray]:
        return self.model.encode(texts, convert_to_numpy=True)
