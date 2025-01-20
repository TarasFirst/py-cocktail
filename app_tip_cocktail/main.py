from typing import Union

from fastapi import FastAPI
# from app_tip_cocktail.models import UserQuery, ChatResponse
# from app_tip_cocktail.chain import init_rag_chain
# from app_tip_cocktail.data_loader import chat_keywords

app = FastAPI(
    title="Cocktail Advisor Chat (Fast API + NumPy + LangChain + FAISS + OpenAI + Llama Index)",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# qa_chain = init_rag_chain()

# @app.post("/chat", response_model=ChatResponse)
# def chat(query: UserQuery):
#
#     pass
