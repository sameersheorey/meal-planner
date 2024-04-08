import sqlite3


class dbShoppingList:
    """A class to manage the shopping list database.

    Attributes:
        db_connection (sqlite3.Connection): A connection to the SQLite database.
    """
        
    def __init__(self, db_name='shopping_list.db'):
        """Initialize a dbShoppingList object and connect to the database.
        
        Args:
            db_name (str, optional): The filename of the SQLite database. Defaults to 'shopping_list.db'.
        """
        self.db_connection = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()


    def create_table(self):
        """Create the 'shoopping list' table if it does not exist."""
        with self.db_connection:
            self.db_connection.execute('''
                CREATE TABLE IF NOT EXISTS menu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ingredient TEXT
                )
            ''')


    def add_ingredients(self, ingredients: list[str]) -> None:
        """Add ingredients to the shopping list.
        
        Args:
            ingredients (list[str]): A list of ingredients.
        """

        for ingredient in ingredients:
            with self.db_connection:                    
                self.db_connection.execute(
                    'INSERT INTO menu (ingredient) VALUES (?)',
                    (ingredient,)
                )
          

    def get_shopping_list(self):
        """Retrieve all ingredients from the shopping list database.

        Returns:
            list[str]: A list of ingredients representing all ingredients in the shopping list database.
        """        
        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM menu")
            dbIngredients = cursor.fetchall()

            ingredients = []
            for shopping_list_item in dbIngredients:
                ingredients.append(shopping_list_item[1])

        return ingredients
    