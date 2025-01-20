import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

FAISS_INDEX_PATH = "embeddings/cocktails.index"
CSV_PATH = "data/cocktails.csv"
INDEX_FOLDER = "embeddings"
