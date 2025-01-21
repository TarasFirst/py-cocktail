import re

import numpy as np
import pandas as pd
from app_tip_cocktail.config import CSV_PATH
from langchain_community.document_loaders import CSVLoader


def load_cocktails_data():
    loader = CSVLoader(file_path=CSV_PATH)
    data = loader.load()
    return data


def load_ingredients_and_cocktails(file_path):
    cocktails_data = pd.read_csv(file_path)
    raw_ingredients = cocktails_data["ingredients"].apply(lambda x: eval(x)).values
    all_ingredients = np.unique(
        np.hstack([
            re.sub(r'[^\w\s]', '', ingredient).strip().lower()
            for sublist in raw_ingredients
            for ingredient in sublist
            if ingredient.strip()
        ])
    )
    all_cocktails = cocktails_data["name"].unique()
    return all_ingredients.tolist(), all_cocktails.tolist()
