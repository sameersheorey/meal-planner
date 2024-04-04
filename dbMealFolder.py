import os
import sqlite3
from bs4 import BeautifulSoup
from MealCard import MealCard
import shutil
import json

class dbMealFolder:
    """A class to manage collections of MealCard objects stored in a database table.

    Attributes:
        db_connection: A connection to the SQLite database.
    """

    def __init__(self, db_name='meal_cards.db'):
        """Initialize a dbMealFolder object and connect to the database.
        
        Args:
            db_name (str, optional): The filename of the SQLite database. Defaults to 'meal_cards.db'.
        """
        self.db_connection = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()


    def create_table(self):
        """Create the 'meal_cards' table if it does not exist."""
        with self.db_connection:
            self.db_connection.execute('''
                CREATE TABLE IF NOT EXISTS meal_cards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT UNIQUE,
                    rating TEXT,
                    metadata TEXT,
                    category TEXT,
                    ingredients TEXT
                )
            ''')


    def add_all(self, filter: str = None) -> None:
        """Generate MealCard objects from all (subject to filter) HTML files in the 'mealData' directory
            and add them to the database.

        Args:
            filter (str, optional): A string representing a filter for categories of meal cards.
            If specified, only meal cards with categories matching the filter will be added.
            Defaults to None, in which case all meal cards are added.
        """
        for file in os.listdir('new_meals'):
            filename = os.fsdecode(file)
            if filename == '.DS_Store':
                continue

            with open(f'new_meals/{filename}', 'r', encoding='utf-8') as file:
                html_content = file.read()

            mealdata = BeautifulSoup(html_content, 'html.parser')
 
            def extract_text(element):
                try:
                    return element.text
                except AttributeError:
                    return "NA"

            title = extract_text(mealdata.find('h1'))
            rating = extract_text(mealdata.find('p', class_="rating"))
            metadata = extract_text(mealdata.find('p', class_="metadata"))
            cats = extract_text(mealdata.find('p', class_="categories"))
            ingredients = [extract_text(ingredient) for ingredient in mealdata.find_all('p', itemprop="recipeIngredient")]
            
            new_mealcard = MealCard(title, rating, metadata, cats, ingredients)

            if filter is None or (filter.casefold() in new_mealcard.cats.casefold()):
                self.add(new_mealcard)

            # Once added move the files in the mealData folder to templates folder

            try:
                shutil.move(os.path.join('new_meals', filename), 'templates/saved_meals')
            except shutil.Error:
                # print("Destination path already exists, overwrite it")
                # shutil.move(os.path.join('mealData', filename), 'templates', copy_function=shutil.copy2)
                pass
            except Exception as e:
                print(f"Error moving {filename} to templates folder: {e}")


    def add(self, meal: MealCard) -> None:
        """Add a MealCard object to the database.

        Args:
            meal (MealCard): The MealCard object to add to the database.

        Raises:
            ValueError: If a meal card with the same title already exists in the database.
        """
        with self.db_connection:
            try:
                # Convert ingredients list to a JSON string
                ingredients_str = json.dumps(meal.ingredients)
                
                self.db_connection.execute(
                    'INSERT INTO meal_cards (title, rating, metadata, category, ingredients) VALUES (?, ?, ?, ?, ?)',
                    (meal.title, meal.rating, meal.metadata, meal.cats, ingredients_str)
                )
            except sqlite3.IntegrityError:
                raise ValueError('Duplicate meal')


    def get_all_meals(self):
        """Retrieve all meal cards from the database.

        Returns:
            list: A list of MealCard objects representing all meal cards in the database.
        """        
        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM meal_cards")
            dbMeals = cursor.fetchall()
            meals = []

            for meal_card in dbMeals:
                # Parse ingredients string into a Python list
                ingredients = json.loads(meal_card[5])

                meal = MealCard(meal_card[1], meal_card[2], meal_card[3], meal_card[4], ingredients)
                meals.append(meal)

        return meals
    
