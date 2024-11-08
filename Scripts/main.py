import logging
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler
from llama_index.core import Settings

llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
Settings.callback_manager = callback_manager

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

from agent_config import AgentConfig
from embedding_config import EmbeddingConfig
from llm_config import LLMConfig
from index_config import IndexConfig
from tool_config import ToolConfig

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

    def run(self):
        # Update the agent system prompt
        print("\t=========")
        self.agent_config.update_system_prompt()
        print("\t=========")
        agent = self.agent_config.get_agent()
        print("\t=========", agent.get_prompts())
        print("Agent is ready for interaction.")

        while True:
            query = input("Enter your question (or 'exit' to quit): ")
            if query.lower() == 'exit':
                print("Exiting.")
                break

            # Query the agent and print the response
            response = agent.query(query)
            print(response)

if __name__ == "__main__":
    manager = AgentManager()
    manager.run()
