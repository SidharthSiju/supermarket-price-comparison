import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from fuzzywuzzy import fuzz, process

# Sample store database with product names
df = pd.read_csv('Aldi.csv')
store_products = df['names'].tolist()


def preprocess_text(text):
    """
    Preprocess the text by lowering case and removing unwanted characters.
    """
    return text.lower().strip()


def match_product_tfidf(user_input, products, threshold=0.3):
    """
    Matches a user input to a list of product names using TF-IDF and cosine similarity.

    :param user_input: The user's input string.
    :param products: List of product names in the store's database.
    :param threshold: Minimum cosine similarity score to consider a match.
    :return: The best matching product and its score.
    """
    # Preprocess the input and products
    user_input = preprocess_text(user_input)
    preprocessed_products = [preprocess_text(p) for p in products]

    # Vectorize the input and products using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_products + [user_input])

    # Calculate cosine similarity between the user input and all products
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    cosine_similarities = cosine_similarities.flatten()

    # Get the best match
    best_match_idx = np.argmax(cosine_similarities)
    best_match_score = cosine_similarities[best_match_idx]

    if best_match_score >= threshold:
        return products[best_match_idx], best_match_score
    else:
        # If TF-IDF fails, fall back to fuzzy matching
        return match_product_fuzzy(user_input, products, threshold=75)


def match_product_fuzzy(user_input, products, threshold=75):
    """
    Matches a user input to a list of product names using fuzzy matching.

    :param user_input: The user's input string.
    :param products: List of product names in the store's database.
    :param threshold: Minimum fuzzy match score to consider a match.
    :return: The best matching product and its score.
    """
    best_match, best_score = process.extractOne(user_input, products)

    if best_score >= threshold:
        return best_match, best_score
    else:
        return None, None


# Example usage
user_input = input("Enter the product you're looking for: ")

matched_product, score = match_product_tfidf(user_input, store_products)

if matched_product:
    print(f"Did you mean: {matched_product}? (Score: {score:.2f})")
else:
    print("No matching product found.")