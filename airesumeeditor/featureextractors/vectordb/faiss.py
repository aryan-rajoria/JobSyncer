import os
from pathlib import Path
from typing import List

import numpy as np

import faiss

class FaissVectorStore:

    def __init__(self):
        self._index = None
        self.dimension = 768
    
    def initialize_index(self):
        self._index = faiss.IndexIDMap2(faiss.IndexHNSWFlat(self.dimension, 32))

    
    def query(self, query_embed, k = 1):
        return self._index.search(query_embed, k)

    def add(self, key, value):
        self._index.add_with_ids(value, key)