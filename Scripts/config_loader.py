# config_loader.py

import os
from dotenv import load_dotenv

class ConfigLoader:
    def __init__(self, env_path='keys.env'):
        self.env_path = env_path
        self.env_vars = {}
        self.load_env_vars()

    def load_env_vars(self):
        load_dotenv(self.env_path)
        self.env_vars = {
            "watsonx_url": os.getenv("WATSONX_URL"),
            "watsonx_apikey": os.getenv("WATSONX_APIKEY"),
            "ibm_project_id": os.getenv("IBM_PROJECT_ID"),
            "qdrant_url": os.getenv("QDRANT_URL"),
            "qdrant_api_key": os.getenv("QDRANT_API_KEY"),
            "openai_api_key": os.getenv("OPENAI_API_KEY"),
        }

    def get_env_vars(self):
        return self.env_vars
