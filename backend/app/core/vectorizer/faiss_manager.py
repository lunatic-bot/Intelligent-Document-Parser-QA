# core/vectorizer/faiss_manager.py
import faiss
import numpy as np
import pickle

class FaissManager:
    def __init__(self, dim, index_path="faiss_index.pkl"):
        self.index = faiss.IndexFlatL2(dim)
        self.index_path = index_path

    def add_embeddings(self, vectors: np.ndarray):
        self.index.add(vectors)

    def save(self):
        faiss.write_index(self.index, self.index_path)

    def load(self):
        self.index = faiss.read_index(self.index_path)
