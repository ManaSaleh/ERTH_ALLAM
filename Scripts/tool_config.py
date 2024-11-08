# tool_config.py

from llama_index.core.tools import QueryEngineTool, ToolMetadata
from prompt_config import PromptTemplates

class ToolConfig:
    def __init__(self, index, embed_model, llm):
        self.index = index
        self.embed_model = embed_model
        self.llm = llm
        self.qa_template = PromptTemplates.create_qa_template()
        self.refine_template = PromptTemplates.create_refine_template()

    def create_tools(self):
        query_tool = QueryEngineTool(
            query_engine=self.index.as_query_engine(
                chat_mode='react',
                embedding=self.embed_model,
                llm=self.llm,
                text_qa_template=self.qa_template,
                refine_template=self.refine_template,
                response_mode="refine",
                verbose=True
            ),
            metadata=ToolMetadata(
                name="query_tool",
                description="A tool for retrieving detailed information about Imam Muhammad bin Saud"
            )
        )

        summarization_tool = QueryEngineTool(
            query_engine=self.index.as_query_engine(
                chat_mode='react',
                embedding=self.embed_model,
                llm=self.llm,
                text_qa_template=self.qa_template,
                refine_template=self.refine_template,
                response_mode="tree_summarize",
                verbose=True
            ),
            metadata=ToolMetadata(
                name="summarization_tool",
                description="A tool for providing summaries."
            )
        )

        subquery_tool = QueryEngineTool(
            query_engine=self.index.as_query_engine(
                chat_mode='react',
                embedding=self.embed_model,
                llm=self.llm,
                text_qa_template=self.qa_template,
                refine_template=self.refine_template,
                response_mode="compact",
                verbose=True
            ),
            metadata=ToolMetadata(
                name="subquery_tool",
                description="A tool for breaking down complex questions into sub-queries."
            )
        )
        tools = [query_tool, summarization_tool, subquery_tool]
        return tools
