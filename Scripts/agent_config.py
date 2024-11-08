# agent_config.py

from llama_index.core.agent import ReActAgent
from llama_index.core.agent.react.formatter import ReActChatFormatter
from formatted_prompt import FormattedPromptConfig

class AgentConfig:
    def __init__(self, tools, llm, max_iterations=10, verbose=True):
        self.tools = tools
        self.llm = llm
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.react_system_prompt = FormattedPromptConfig().get_prompt()
        self.agent = self._initialize_agent()

    def _initialize_agent(self):
        # Create and configure the ReActAgent
        agent = ReActAgent.from_tools(
            tools=self.tools,
            verbose=self.verbose,
            max_iterations=self.max_iterations,
            llm=self.llm,
            formatter=ReActChatFormatter.from_defaults(),
            # memory=chat_memory_buffer  # Uncomment if you need memory buffer
            # force_tool_usage=True     # Uncomment to force tool usage
        )
        return agent

    def update_system_prompt(self):
        # Update the system prompt for the agent
        self.agent.update_prompts({"agent_worker:system_prompt": self.react_system_prompt})

    def get_agent(self):
        return self.agent
