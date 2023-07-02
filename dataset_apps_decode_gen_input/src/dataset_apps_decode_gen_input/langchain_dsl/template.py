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
from . import OPENAI_API_KEY, SYSTEM_TEMPLATE, HUMAN_TEMPLATE, QUESTION_2, DSL_2


def dsl_template():
    system_message_prompt = SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE)
    human_message_prompt = HumanMessagePromptTemplate.from_template(HUMAN_TEMPLATE)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    msg = chat_prompt.format_messages(
        question=QUESTION_2,
    )

    return msg
