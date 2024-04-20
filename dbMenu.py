import random
import sqlite3
from MealCard import MealCard
from MenuItem import MenuItem
from datetime import datetime


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


    def create_table(self) -> None:
        """Create the 'menu' table if it does not exist."""

        with self.db_connection:
            self.db_connection.execute('''
                CREATE TABLE IF NOT EXISTS menu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT UNIQUE,
                    meal_id INTEGER,
                    added_to_shopping INTEGER DEFAULT 0                   
                )
            ''')


    def add_random_meal(self, meal_cards: list[MealCard], date: str) -> None:
        """Add a randomly selected meal from the provided list of MealCards to the weekly menu.
        
        Args:
            meal_cards (list[MealCard]): A list of MealCard objects to choose a meal from.
        """

        meal = random.choice(meal_cards)

        newdate = date
       
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
        """Replace a meal in the menu with a randomly selected meal from the provided list of MealCards and reset 'added_to_shopping' to 0.

            Args:
                meal_cards (list[MealCard]): A list of MealCard objects to choose a new meal from.
                menu_id (int): The ID of the menu item to replace.
        """
        
        new_meal = random.choice(meal_cards)

        with self.db_connection:
            self.db_connection.execute(
                'UPDATE menu SET meal_id = ?, added_to_shopping = 0 WHERE id = ? ',
                [new_meal.id, menu_id]
            )
       

    def date_in_menu(self, date: str) -> bool:
        """Check a meal for a given date is in the menu.

        Args:
            date (str): The date of the menu to retrieve.
            
        Returns:
            bool: True if a menu item exists for the given date, False otherwise.
        """

        with self.db_connection:
            cursor = self.db_connection.cursor()
            

            cursor.execute("SELECT * FROM menu WHERE date = ?", [date])
            
            dbMenu = cursor.fetchall()

            if dbMenu:
                return True

            else: 
                return False

    def get_menu_item_by_date(self, date: str) -> MealCard:
        """Retrieve a menu from the database by its date.

        Args:
            date (str): The date of the menu to retrieve.
            
        Returns:
            MenuItem: A MenuItem object representing the menu item with the given date.
        """

        with self.db_connection:
            cursor = self.db_connection.cursor()
            
   
            cursor.execute("SELECT * FROM menu WHERE date = ?", [date])
            
            dbMenu = cursor.fetchall()

            if dbMenu:
                row = dbMenu[0]
                menu_item = MenuItem(row[0], row[1], row[2], row[3])
                return menu_item

            else: 
                return None
    

    def get_menu(self, order_by_date: bool = False) -> list[MenuItem]:
        """Retrieve all menu items from the database.

        Args:
            order_by_date (bool, optional): Whether to order the results by date. Defaults to False.

        Returns:
            list[MenuItem]: A list of MenuItem objects representing all menu items in the database.
        """        

        with self.db_connection:
            cursor = self.db_connection.cursor()

            if order_by_date:
                cursor.execute("SELECT * FROM menu ORDER BY date")  
            else: 
                cursor.execute("SELECT * FROM menu")
   
            dbMenu = cursor.fetchall()

            menu = []
            for row in dbMenu:
                menu_item = MenuItem(row[0], row[1], row[2], row[3])
                menu.append(menu_item)

        return menu
    

    def toggle_added_to_shopping(self, menu_id) -> None:
        """Toggle the value of the 'added_to_shopping' column for a specific menu item.

        Args:
            menu_id (int): The ID of the menu item to toggle.
        """
            
        with self.db_connection:
            current_value = self.db_connection.execute(
                'SELECT added_to_shopping FROM menu WHERE id = ?',
                (menu_id,)
            ).fetchone()[0]

            new_value = 1 if current_value == 0 else 0

            self.db_connection.execute(
                'UPDATE menu SET added_to_shopping = ? WHERE id = ? ',
                (new_value, menu_id)
            )

    