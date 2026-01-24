from typing import List
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        self.model = SentenceTransformer(model_name)
    
    def encode(self, text: str) -> List[float]:
        vec = self.model.encode(text)
        return vec.tolist()