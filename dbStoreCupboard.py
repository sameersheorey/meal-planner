import sqlite3
from dbIngredients import dbIngredients
from difflib import SequenceMatcher
from utils import similar

class dbStoreCupboard(dbIngredients):
    """A class to manage the store cupboard database.

    Attributes:
        db_connection (sqlite3.Connection): A connection to the SQLite database.
    """

    def find_similar_ingredients(self, new_ingredients, similarity_threshold = 0.7):
        store_cupboard = self.get_ingredients_list()
        store_comparison = {}
        for store_ingredient in store_cupboard:
            similar_ingredients = []
            for new_ingredient in new_ingredients:
                similarity = similar(store_ingredient, new_ingredient)
                if similarity > similarity_threshold:
                    similar_ingredients.append(new_ingredient)
            if similar_ingredients:
                store_comparison[store_ingredient] = similar_ingredients
        return store_comparison
