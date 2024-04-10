import random
import sqlite3
from MealCard import MealCard
from MenuItem import MenuItem
import datetime


class dbMenu:
    """A class to manage the menu database.

    Attributes:
        db_connection (sqlite3.Connection): A connection to the SQLite database.
    """
        
    def __init__(self, db_name='menu.db'):
        """Initialize a dbMenus object and connect to the database.
        
        Args:
            db_name (str, optional): The filename of the SQLite database. Defaults to 'menu.db'.
        """
        
        self.db_connection = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()


    def create_table(self):
        """Create the 'menu' table if it does not exist."""

        with self.db_connection:
            self.db_connection.execute('''
                CREATE TABLE IF NOT EXISTS menu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT UNIQUE,
                    meal_id INTEGER
                )
            ''')


    def add_random_meal(self, meal_cards: list[MealCard]) -> None:
        """Add a randomly selected meal from the provided list of MealCards to the weekly menu.
        
        Args:
            meal_cards (list[MealCard]): A list of MealCard objects to choose a meal from.
        """

        meal = random.choice(meal_cards)

        newdate = datetime.datetime.now()

        with self.db_connection:
            try:                
                self.db_connection.execute(
                    'INSERT INTO menu (date, meal_id) VALUES (?, ?)',
                    (newdate, meal.id)
                )
            except sqlite3.IntegrityError:
                raise ValueError('Duplicate date')
            
    
    def delete_menu_item_by_menu_id(self, menu_id: int) -> None:
        """Delete the menu item with a particular meal_id.

        Args:
            menu_id (int): ID of the meal.
        """
        with self.db_connection:
            self.db_connection.execute(
                'DELETE FROM menu WHERE id = ?',
                (menu_id,)
            )


    def replace_menu_item(self, meal_cards: list[MealCard], menu_id: int)-> None:
        
        new_meal = random.choice(meal_cards)

        with self.db_connection:
            self.db_connection.execute(
                'UPDATE menu SET meal_id = ? WHERE id = ? ',
                [new_meal.id, menu_id]
            )
       

    def get_menu(self):
        """Retrieve all menu items from the database.

        Returns:
            list[MenuItem]: A list of MenuItem objects representing all menu items in the database.
        """        

        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM menu")
            dbMenu = cursor.fetchall()

            menu = []
            for meal in dbMenu:
                menu_item = MenuItem(meal[0], meal[1], meal[2])
                menu.append(menu_item)

        return menu
    