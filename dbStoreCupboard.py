import sqlite3
from dbIngredients import dbIngredients
from difflib import SequenceMatcher
from utils import similar

class dbStoreCupboard(dbIngredients):
    """A class to manage the store cupboard database."""

    def find_similar_ingredients(self, 
                                 new_ingredients: list[str], 
                                 similarity_threshold: float = 0.7
                                 ) -> dict[str, list[str]]:
        """
        Find similar ingredients from the store cupboard based on a similarity threshold.

        Args:
            new_ingredients (list[str]): A list of new ingredients to compare against.
            similarity_threshold (float, optional): The threshold for considering ingredients similar.
                Defaults to 0.7.

        Returns:
            dict[str, list[str]]: A dictionary where keys are ingredients from the store cupboard
            and values are lists of similar ingredients from the new_ingredients list.
        """

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
