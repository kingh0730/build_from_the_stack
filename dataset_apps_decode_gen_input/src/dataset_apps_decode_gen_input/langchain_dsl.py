from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage


def i_love_programming():
    chat = ChatOpenAI(temperature=0)
    ans = chat.predict_messages(
        [
            HumanMessage(
                content="Translate this sentence from English to French. I love programming."
            )
        ]
    )
    return ans
