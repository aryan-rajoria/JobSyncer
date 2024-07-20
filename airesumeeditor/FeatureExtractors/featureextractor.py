from torch import Tensor
class SentenceTransformer:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L12-v2")

    def generate_embeddings(self, text: str) -> List[float]:
        embedding = self.model.encode(input)
        return embedding

    def similarity(self, embed_matrix_1, embed_matrix_2) -> Tensor:
        similarities = self.model.similarity(embed_matrix_1, embed_matrix_2)
        return similarities