import random
import sqlite3
from MealCard import MealCard
from Menu import Menu
import datetime

class dbMenu:
    """A class to manage weekly menus.

    Attributes:
        menus (list): A list to store weekly menus.
        menu_titles (list): A list to store weekly menu titles.
        ingredients (list): A list to store weekly ingredients.
    """
        
    def __init__(self, db_name='menus.db'):
        """Initialize a dbMenus object and connect to the database.
        
        Args:
            db_name (str, optional): The filename of the SQLite database. Defaults to 'menus.db'.
        """
        self.db_connection = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()


    # THIS DATABASE SHOULD HAVE ROWS WITH A DATE AND A LINK TO THE ID OF A MEAL IN THE MEAL DATABASE
    def create_table(self):
        """Create the 'menu' table if it does not exist."""
        with self.db_connection:
            self.db_connection.execute('''
                CREATE TABLE IF NOT EXISTS menu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT UNIQUE,
                    title TEXT
                )
            ''')


    # GET ALL MEALCARDS FROM THE MEALCARD DATABASE (COMES OUT AS A LIST) AND THEN RANDOMLY SELECT ONE
    # WE ALSO WANT INGREDIENTS BUT WHEN WE REFERENCE TO THE MEAL DATABASE THIS WILL HAVE ALL INGREDIENTS
    # NEED TO THINK ABOUT HOW TO ADD AND STORE INGREDIENTS 

    def add_random_meal(self, meal_cards: list[MealCard]) -> None:
        """Add a menu to the list of weekly menus, the menu titles to the list of weekly menu titles
          and the ingredients from that menus to the list of weekly ingredients
        
        Args:
            meal_folder (MealFolder): The MealFolder object from which to generate the menu.
            menu_generator (str, optional): The type of menu generator to use. Defaults to "random".
        """
        meal = random.choice(meal_cards)

        newdate = datetime.datetime.now()

        with self.db_connection:
            try:
                # REALLY WANT TO LINK TO THE MEAL IN THE OTHER DATABASE SOMEHOW WITH THE ID. AS PLACEHOLDER PUT MEAL.TITLE
                
                self.db_connection.execute(
                    'INSERT INTO menu (date, title) VALUES (?, ?)',
                    (newdate, meal.title)
                )
            except sqlite3.IntegrityError:
                raise ValueError('Duplicate date')


    # INSTEAD OF MENU DICTIONARY MAKE A MENU CLASS LIKE THE MEAL CARD CLASS
    def get_menu(self):
        """Retrieve all meal cards from the database.

        Returns:
            list: A list of MealCard objects representing all meal cards in the database.
        """        
        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM menu")
            dbMeals = cursor.fetchall()

            menu = []
            for meal in dbMeals:
                menu_item = Menu(meal[1], meal[2])
                menu.append(menu_item)

        return menu
    