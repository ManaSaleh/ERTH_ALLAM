# index_config.py

from llama_index.core import VectorStoreIndex
from qdrant_config import QdrantConfig

class IndexConfig:
    def __init__(self):
        # Initialize QdrantConfig to get the vector store
        self.qdrant_config = QdrantConfig()
        self.vector_store = self.qdrant_config.get_vector_store()
        
        # Setup the vector store index
        self.index = VectorStoreIndex.from_vector_store(vector_store=self.vector_store)

    def get_index(self):
        return self.index
