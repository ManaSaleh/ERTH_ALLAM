# embedding_config.py

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from config_loader import ConfigLoader

class EmbeddingConfig:
    def __init__(self, model="text-embedding-ada-002", embed_batch_size=10):
        # Load environment variables using ConfigLoader
        self.config_loader = ConfigLoader()
        self.env_vars = self.config_loader.get_env_vars()

        # Initialize the OpenAI embedding model with the API key and parameters
        self.embed_model = OpenAIEmbedding(
            api_key=self.env_vars["openai_api_key"],
            model=model,
            embed_batch_size=embed_batch_size
        )

        # Assign embed_model to Settings
        Settings.embed_model = self.embed_model

    def get_embed_model(self):
        return self.embed_model
