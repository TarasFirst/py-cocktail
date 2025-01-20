from app_tip_cocktail.config import CSV_PATH

from langchain_community.document_loaders import CSVLoader


def load_cocktails_data():
    loader = CSVLoader(file_path=CSV_PATH)
    data = loader.load()
    return data
