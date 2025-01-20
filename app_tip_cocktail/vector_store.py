import openai
import faiss
import numpy as np

dimension = 1536
index = faiss.IndexFlatL2(dimension)
metadata_store = []


def get_embedding(text: str) -> list:
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response["data"][0]["embedding"]


def extract_preferences(message: str) -> list:

    system_message = "Determine if the text mentions favorite cocktails or ingredients, and return a list of what was found in JSON format."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": message}
        ]
    )
    try:
        extracted = response["choices"][0]["message"]["content"]
        return eval(extracted)  # Перетворення JSON на Python-об'єкт
    except Exception as e:
        return []


def add_to_index(text: str, metadata: dict):

    vector = np.array([get_embedding(text)])
    index.add(vector)
    metadata_store.append({"text": text, "metadata": metadata})


def search_in_index(query: str, k=5) -> list:

    query_vector = np.array([get_embedding(query)])
    distances, indices = index.search(query_vector, k)
    return [metadata_store[i] for i in indices[0] if i < len(metadata_store)]
