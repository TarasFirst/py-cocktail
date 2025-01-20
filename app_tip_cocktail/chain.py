import getpass
import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from config import OPENAI_API_KEY

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]


def return_answer(chat_messages):
    return model.invoke(chat_messages).content


print(return_answer(messages))
