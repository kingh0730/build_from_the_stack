from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import openai
from . import OPENAI_API_KEY, TEMPLATE


def dsl_template():
    system_message_prompt = SystemMessagePromptTemplate.from_template(TEMPLATE)
    human_template = "{question}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    msg = chat_prompt.format_messages(
        input_language="English",
        output_language="French",
        text="I love programming.",
    )

    return msg
