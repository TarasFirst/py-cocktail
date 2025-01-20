import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CSV_PATH = "data/cocktails.csv"

# FAISS_INDEX_PATH = "embeddings/cocktails.index"
# INDEX_FOLDER = "embeddings"
