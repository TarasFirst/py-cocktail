import getpass
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app_tip_cocktail.load_data import load_cocktails_data
from app_tip_cocktail.config import OPENAI_API_KEY
from app_tip_cocktail.vector_store import extract_preferences, add_to_index, search_in_index


def chain_main(message):
    model = ChatOpenAI(model="gpt-4o-mini")

    if not os.environ.get("OPENAI_API_KEY"):
      os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

    system_template = ("Use the found preferences and information from saved memory to create a response. "
                       "If there is no relevant information, respond based on the query only.")

    preferences = extract_preferences(message)

    if preferences:
        for pref in preferences:
            add_to_index(pref["name"], {"type": pref["type"], "name": pref["name"]})

    content = load_cocktails_data()

    relevant_data = search_in_index(message)

    chat_messages = [
        {"role": "system", "content": system_template},
        {"role": "user", "content": message},
        {"role": "assistant", "content": f"Знайдені уподобання: {relevant_data}"}
    ]

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    prompt = prompt_template.invoke({"content": content, "text": message})


    response = model.invoke(prompt)

    return response.content
