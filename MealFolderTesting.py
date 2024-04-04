import os
from bs4 import BeautifulSoup
from MealCard import MealCard
import shutil

class MealFolder:
    """A class to manage collections of MealCard objects.

    Attributes:
        titles (list): A list to store titles of meal cards.
        mealcards (list): A list to store MealCard objects.
    """

    def __init__(self):
        """Initialize a MealFolder object.
        
        Creates an empty list to store titles and another empty list to store MealCard objects.
        """
        
        self.titles = []
        self.mealcards = []
        

    def add_all(self, filter: str = None) -> None:
        """Generate MealCard objects from all (subject to filter) HTML files in the 'mealData' directory
            and add them to the database.

        Args:
            filter (str, optional): A string representing a filter for categories of meal cards.
            If specified, only meal cards with categories matching the filter will be added.
            Defaults to None, in which case all meal cards are added.
        """
        for file in os.listdir('mealData'):
            filename = os.fsdecode(file)
            if filename == '.DS_Store':
                continue

            with open(f'mealData/{filename}', 'r', encoding='utf-8') as file:
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

            # Once added move the files in the mealData folder to a new folder called templates

            try:
                shutil.move(os.path.join('mealData', filename), 'templates')
            except shutil.Error:
                print("Destination path already exists, overwrite it")
                shutil.move(os.path.join('mealData', filename), 'templates', copy_function=shutil.copy2)
            except Exception as e:
                print(f"Error moving {filename} to templates folder: {e}")


    
    def add(self, meal: MealCard) -> None:
        """Add a MealCard object to the MealFolder.
        
        Args:
            meal (MealCard): The MealCard object to add to the MealFolder.

        Raises:
            TypeError: If the provided argument is not a MealCard object.
            ValueError: If a meal card with the same title already exists in the MealFolder.
        """
        if type(meal) != MealCard: raise TypeError('not a meal card')
        if meal.title in self.titles: raise ValueError('duplicate meal')
        self.titles.append(meal.title)
        self.mealcards.append(meal)
                
    def __iter__(self):
        """Return an iterator over the MealFolder's meal cards.
        
        Returns:
            iterator: An iterator over the meal cards stored in the MealFolder.
        """
        return iter(self.mealcards)