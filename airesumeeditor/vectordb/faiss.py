import os
from pathlib import Path
from typing import List

import numpy as np

import faiss

class FaissVectorStore:

    def __init__(self):
        self._index1 = None
        self.index2 = None
        self.dimension = 768
    
    def initialize_index(self):
        self._index1 = faiss.IndexIDMap2(faiss.IndexHNSWFlat(self.dimension, 32))
        self.index2 = faiss.IndexIDMap2(faiss.IndexHNSWFlat(self.dimension, 32))

    
    def query1(self, query_embed, k = 1):
        return self._index1.search(query_embed, k)

    def add1(self, key, value):
        self._index1.add_with_ids(value, key)

    def query2(self, query_embed, k = 1):
        return self._index1.search(query_embed, k)

    def add2(self, key, value):
        self._index1.add_with_ids(value, key)