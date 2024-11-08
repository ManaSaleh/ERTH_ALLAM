# llm_config.py

from llama_index.llms.ibm.base import WatsonxLLM
from config_loader import ConfigLoader

class LLMConfig:
    def __init__(self, model_id="sdaia/allam-1-13b-instruct", max_new_tokens=200):
        # Load environment variables using ConfigLoader
        self.config_loader = ConfigLoader()
        self.env_vars = self.config_loader.get_env_vars()
        
        # Initialize the LLM model with parameters
        self.llm = WatsonxLLM(
            model_id=model_id,
            credentials={
                "url": self.env_vars["watsonx_url"],
                "apikey": self.env_vars["watsonx_apikey"],
            },
            project_id=self.env_vars["ibm_project_id"],
            max_new_tokens=max_new_tokens,
            additional_params={
                "decoding_method": "greedy",
                "beam_width": 10,
                "repetition_penalty": 1,
                "temperature": 1,
            },
            context_window=4096,
        )

    def get_llm(self):
        return self.llm
