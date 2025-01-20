import pandas as pd

from app_tip_cocktail.config import CSV_PATH

def load_cocktails_data():
    df = pd.read_csv(CSV_PATH)
    needed_cols = ["name", "ingredients", "alcoholic"]
    missing_cols = [col for col in needed_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Required columns {missing_cols} not found in {CSV_PATH}")
    return df[needed_cols].dropna()


def chat_keywords():
    df = load_cocktails_data()

    unique_ingredients = set(
        ingr.strip().lower()
        for ingr_list in df["ingredients"].dropna()
        for ingr in ingr_list.split(", ")
    )
    cocktails = set(df["name"].str.lower().dropna())
    keywords = {"cocktail", "cocktail", "drink", "ingredient", "ingredients","recipe", "mix", "alcohol", "liquor", "bar", "taste", "flavor"}

    keywords.update(unique_ingredients)
    keywords.update(cocktails)

    cleaned_keywords = set(
        word.strip("'[]").lower() for word in keywords
    )

    return list(cleaned_keywords)
