import sqlite3


class dbIngredients:
    """A class to manage a database of ingredients.

    Attributes:
        db_connection (sqlite3.Connection): A connection to the SQLite database.
    """
        
    def __init__(self, db_name):
        """Initialize a dbIngredients object and connect to the database.
        
        Args:
            db_name (str): The filename of the SQLite database.
        """
        self.db_connection = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()


    def create_table(self):
        """Create the 'Ingredients' table if it does not exist."""
        with self.db_connection:
            self.db_connection.execute('''
                CREATE TABLE IF NOT EXISTS ingredients_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ingredient TEXT,
                    menu_id INTEGER
                )
            ''')


    def add_ingredients(self, ingredients: list[str], menu_id: int = None) -> None:
        """Add ingredients to the ingredients list.
        
        Args:
            ingredients (list[str]): A list of ingredients.
            menu_id (int, optional): ID of the menu item assiciated with ingredients (if there is one). Defaults to None.
        """
        with self.db_connection:
            for ingredient in ingredients:
                self.db_connection.execute(
                    'INSERT INTO ingredients_table (ingredient, menu_id) VALUES (?, ?)',
                    (ingredient, menu_id)
                )
          

    def get_ingredients_list(self):
        """Retrieve all ingredients from the ingredient list database.

        Returns:
            list[str]: A list of ingredients representing all ingredients in the ingredient list database.
        """        
        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM ingredients_table")
            dbIngredients = cursor.fetchall()

            ingredients = []
            for ingredient_list_item in dbIngredients:
                ingredients.append(ingredient_list_item[1])

        return ingredients
    