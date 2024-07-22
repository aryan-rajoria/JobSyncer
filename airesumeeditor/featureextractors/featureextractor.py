from torch import Tensor
from typing import List
from sentence_transformers import SentenceTransformer

class SentenceEmbedder:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L12-v2")

    def generate_embeddings(self, text):
        embedding = self.model.encode(text)
        return embedding

    def similarity(self, embed_matrix_1, embed_matrix_2) -> Tensor:
        similarities = self.model.similarity(embed_matrix_1, embed_matrix_2)
        return similarities