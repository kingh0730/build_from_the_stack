from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import openai
from . import OPENAI_API_KEY


def i_love_programming():
    print(openai.api_key)
    chat = ChatOpenAI(
        temperature=0,
        openai_api_key=OPENAI_API_KEY,
    )
    ans = chat.predict_messages(
        [
            HumanMessage(
                content="Translate this sentence from English to French. I love programming."
            )
        ]
    )
    return ans
