# app.py

import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler
from llama_index.core import Settings

from agent_config import AgentConfig
from embedding_config import EmbeddingConfig
from llm_config import LLMConfig
from index_config import IndexConfig
from tool_config import ToolConfig

# Set up logging and debugging
llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
Settings.callback_manager = callback_manager

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

# Define FastAPI app
app = FastAPI()

# Define request model
class QueryRequest(BaseModel):
    query: str

# Agent manager setup
class AgentManager:
    def __init__(self):
        # Initialize configurations
        self.embedding_config = EmbeddingConfig()
        self.llm_config = LLMConfig()
        self.index_config = IndexConfig()
        
        # Retrieve components
        self.embed_model = self.embedding_config.get_embed_model()
        self.llm = self.llm_config.get_llm()
        self.index = self.index_config.get_index()
        
        # Set up tools
        self.tool_config = ToolConfig(self.index, self.embed_model, self.llm)
        self.tools = self.tool_config.create_tools()

        # Initialize the agent
        self.agent_config = AgentConfig(
            tools=self.tools,
            llm=self.llm
        )
        self.agent_config.update_system_prompt()
        self.agent = self.agent_config.get_agent()

    def query_agent(self, query):
        # Query the agent and reset memory after each query
        response = self.agent.query(query)
        self.agent.memory.reset()
        return response

# Initialize AgentManager
agent_manager = AgentManager()

@app.post("/query")
async def query(request: QueryRequest):
    """
    Endpoint to query the agent with a question.
    """
    try:
        response = agent_manager.query_agent(request.query)
        return {"response": response}
    except Exception as e:
        logging.error(f"Error querying agent: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the query.")
