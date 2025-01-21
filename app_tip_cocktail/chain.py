import os
import getpass

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from llama_index.core import Document, VectorStoreIndex, StorageContext, load_index_from_storage

from app_tip_cocktail.config import CSV_PATH
from app_tip_cocktail.llama_index_store import create_and_save_index_with_faiss, load_index_and_query_with_faiss
from app_tip_cocktail.load_data import load_cocktails_data, load_ingredients_and_cocktails

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

def update_favourite_items(query, ingredients, cocktails):
    raw_data = query.split(", ")
    store_data = []
    for word in raw_data:
        if word in ingredients:
            store_data.append(word)
        if word in cocktails:
            store_data.append(word)
    return ", ".join(store_data)


def chain_main(message, file_path=CSV_PATH):

    faiss_index_path = "faiss_index.bin"
    storage_path = "index_storage"

    all_ingredients, all_cocktails = load_ingredients_and_cocktails(file_path)

    if not os.path.exists(faiss_index_path):
        print("FAISS index not found. Creating a new one...")
        documents = [
            Document(text="I like ...", metadata={"type": "info"}),
            Document(text="Can you help me?", metadata={"type": "query"})
        ]
        create_and_save_index_with_faiss(documents, storage_path, faiss_index_path)



    relevant_data = load_index_and_query_with_faiss(message, storage_path, faiss_index_path)
    found_ingredients = [ingredient for ingredient in all_ingredients if ingredient.lower() in message.lower()]
    found_cocktails = [cocktail for cocktail in all_cocktails if cocktail.lower() in message.lower()]
    keywords = ["cocktail", "drink", "ingredient", "recipe", "mix", "alcohol", "liquor",
                "bar", "taste", "flavor"]
    # found_keywords = [word for word in keywords if word in message.lower()]

    if found_ingredients:
        ingredients = ', '.join(found_ingredients)
        print(f"found_ingredients: {ingredients}")
    else:
        ingredients = ""
    if found_cocktails:
        cocktails = ', '.join(found_cocktails)
        print(f"found_cocktails: {cocktails}")
    else:
        cocktails = ""

    add_favourite = ingredients + cocktails

    if add_favourite:
        load_index = load_index_and_query_with_faiss(add_favourite, storage_path, faiss_index_path)
        new_document = Document(text=load_index, metadata={"type": "info"})
        create_and_save_index_with_faiss([new_document], storage_path, faiss_index_path)

    if update_favourite_items(message, all_ingredients, all_cocktails):
        favourite_data = update_favourite_items(message, all_ingredients, all_cocktails)
        print(f"favourite_data: {favourite_data}")

    content = load_cocktails_data()



    system_template = ("You are a helpful assistant. Use {relevant_data} data to answer"
                      "If no {relevant_data}, respond based on {content}.")

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_template),
            ("user", "{text}")
        ]
    )

    model = ChatOpenAI(model="gpt-4o-mini")
    prompt = prompt_template.invoke({"relevant_data": relevant_data, "text": message, "content": content, "favourite_ingredients": favourite_data})
    response = model.invoke(prompt)

    return response.content
