import sqlite3
from dbIngredients import dbIngredients

class dbShoppingList(dbIngredients):
    """A class to manage the shopping list database.

    Attributes:
        db_connection (sqlite3.Connection): A connection to the SQLite database.
    """
        
    def delete_ingredients_by_meal_id(self, menu_id: int) -> None:
        """Delete all ingredients with a particular meal_id.

        Args:
            meal_id (int): ID of the meal.
        """
        with self.db_connection:
            self.db_connection.execute(
                'DELETE FROM menu WHERE menu_id = ?',
                (menu_id,)
            )