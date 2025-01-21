from fastapi import FastAPI
from pydantic import BaseModel

from app_tip_cocktail.chain import chain

app = FastAPI(
    title="Cocktail Advisor Chat (Fast API + LangChain + OpenAI)",
    version="0.1.0",
)


class UserQuery(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@app.post("/tip", response_model=ChatResponse)
def give_tip(query: UserQuery) -> ChatResponse:
    """
    Replace the "string" with your question about cocktails or ingredients.
    You'll get the answer based on the existing data set cocktails.csv.
    """
    answer = chain(query.question)
    return ChatResponse(answer=answer)
