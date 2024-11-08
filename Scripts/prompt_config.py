# prompt_config.py

from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate

class CustomSystemMessage:
    @staticmethod
    def get_message():
        return "أجب بإيجاز وبأسلوب يجمع بين اللغة العربية الرسمية واللهجة النجدية بشكل طبيعي. تجنب تكرار الإجابة وقدمها كجزء واحد متكامل."

class PromptTemplates:
    @staticmethod
    def create_qa_template():
        qa_prompt_str = (
            "المعلومات السياقية أدناه.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "بناءً على المعلومات السياقية ودون معرفة مسبقة، "
            "أجب على السؤال باللهجة النجدية وبصيغة رسمية دون تكرار: {query_str}\n"
        )
        chat_text_qa_msgs = [
            ChatMessage(
                role=MessageRole.SYSTEM,
                content="أجب عن السؤال دائمًا، حتى إذا لم يكن السياق مفيدًا"
            ),
            ChatMessage(role=MessageRole.USER, content=qa_prompt_str),
        ]
        return ChatPromptTemplate(chat_text_qa_msgs)

    @staticmethod
    def create_refine_template():
        refine_prompt_str = (
            "لدينا فرصة لتحسين الإجابة الأصلية "
            "(فقط إذا لزم الأمر) مع المزيد من السياق أدناه.\n"
            "------------\n"
            "{context_msg}\n"
            "------------\n"
            "بناءً على السياق الجديد، قم بتحسين الإجابة الأصلية باللهجة النجدية "
            "لتكون إجابة واحدة متكاملة ودون تكرار للسؤال: {query_str}. "
            "إذا لم يكن السياق مفيدًا، قدم الإجابة الأصلية نفسها.\n"
            "الإجابة الأصلية: {existing_answer}"
        )
        chat_refine_msgs = [
            ChatMessage(
                role=MessageRole.SYSTEM,
                content="أجب عن السؤال دائمًا، حتى إذا لم يكن السياق مفيدًا"
            ),
            ChatMessage(role=MessageRole.USER, content=refine_prompt_str),
        ]
        return ChatPromptTemplate(chat_refine_msgs)
