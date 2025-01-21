import getpass
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app_tip_cocktail.load_data import load_cocktails_data


def chain(message: str) ->  str | list[str | dict]:
    model = ChatOpenAI(model="gpt-4o-mini")
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(
            "Enter API key for OpenAI: "
        )
    system_template = "Give tips about {content}"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )
    content = load_cocktails_data()
    prompt = prompt_template.invoke({"content": content, "text": message})
    response = model.invoke(prompt)
    return response.content
