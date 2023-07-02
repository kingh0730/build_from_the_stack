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
from . import (
    OPENAI_API_KEY,
    SYSTEM_TEMPLATE,
    HUMAN_TEMPLATE,
    QUESTION_2,
    DSL_2,
    QUESTION_1,
    DSL_1,
)


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


def dsl_chain():
    chat = ChatOpenAI(
        temperature=0,
        model="gpt-4",
        openai_api_key=OPENAI_API_KEY,
    )

    system_message_prompt = SystemMessage(content=SYSTEM_TEMPLATE)
    human_message_prompt = HumanMessagePromptTemplate.from_template(HUMAN_TEMPLATE)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    ans = chain.run(
        question=QUESTION_1,
    )

    return ans
