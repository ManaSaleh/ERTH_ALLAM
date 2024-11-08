# qdrant_config.py

from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore
from config_loader import ConfigLoader

class QdrantConfig:
    def __init__(self, collection_name="collection"):
        # Load environment variables using ConfigLoader
        self.config_loader = ConfigLoader()
        self.env_vars = self.config_loader.get_env_vars()

        # Initialize the Qdrant client
        self.qdrant_client = QdrantClient(
            url=self.env_vars["qdrant_url"],
            api_key=self.env_vars["qdrant_api_key"]
        )
        
        # Setup the vector store
        self.collection_name = collection_name
        self.vector_store = QdrantVectorStore(
            client=self.qdrant_client,
            collection_name=self.collection_name
        )

    def get_qdrant_client(self):
        return self.qdrant_client

    def get_vector_store(self):
        return self.vector_store
