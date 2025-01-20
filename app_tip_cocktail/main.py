from fastapi import FastAPI
from pydantic import BaseModel

from app_tip_cocktail.chain import chain_main


app = FastAPI(
    title="Cocktail Advisor Chat (Fast API + NumPy + LangChain + FAISS + OpenAI + Llama Index)",
    version="0.1.0"
)


class UserQuery(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@app.post("/tip", response_model=ChatResponse)
def give_tip(query: UserQuery):
    answer = chain_main(query.question)
    return ChatResponse(answer=answer)
