from typing import List

from langchain_community.document_loaders import CSVLoader
from langchain_core.documents import Document

from app_tip_cocktail.config import CSV_PATH


def load_cocktails_data() -> list[Document]:
    loader = CSVLoader(file_path=CSV_PATH)
    data = loader.load()
    return data
