import os
from bs4 import BeautifulSoup

class MealCard:
     def __init__(self, mealdata):
        """Initialize the MealCard object with data from a meal HMTL file.
        
        Args:
            mealdata: BeautifulSoup object representing the HTML content of a meal HTML file.
        """
        
        self.title = mealdata.find('h1')
        self.rating = mealdata.find('p', class_="rating")
        self.metadata = mealdata.find('p', class_="metadata")
        self.cats = mealdata.find('p', class_="categories")
        self.ingredients = mealdata.find_all('p', itemprop="recipeIngredient")


class MealFolder:
    def __init__(self):
        """Initialize a MealFolder object.
        
        Creates an empty list to store titles and another empty list to store MealCard objects.
        """
        self.titles = []
        self.mealcards = []
        
    def add_all(self, filter = None):
        """Generate MealCard objects from all (subject to filter) HTML files in the 'mealData' directory
            and add to the MealFolder object.
        
        Args:
            filter (str, optional): A string representing a filter for categories of meal cards. 
            If specified, only meal cards with categories matching the filter will be added. 
            Defaults to None, in which case all meal cards are added.
        """

        for file in os.listdir('mealData'):
            # Open the HTML files
            filename = os.fsdecode(file)
            
            if filename == '.DS_Store':
                continue

            with open(f'mealData/{filename}', 'r', encoding='utf-8') as file:
                # Read the contents of the file
                html_content = file.read()

            # Create a BeautifulSoup object
            mealdata = BeautifulSoup(html_content, 'html.parser')

            # Create a meal card
            new_mealcard = MealCard(mealdata)

            # If no filter is specified add meal card
            if filter is None:
                self.add(new_mealcard)

            # If filter specified on add only meal cards satisfying the filter
            elif new_mealcard.cats is not None and filter.casefold() in new_mealcard.cats.text.casefold():
                self.add(new_mealcard)
        
    def get_mealcard(self, title):
        """Retrieve a MealCard object from the MealFolder by its title.

        Args:
            title (str): The title of the meal card to retrieve.

        Returns:
            MealCard: The MealCard object with the specified title.

        Raises:
            ValueError: If no meal card with the specified title is found.
        """
        for meal_card in self:
            if meal_card.title.text == title:
                return meal_card
        raise ValueError(f'Meal with title "{title}" not found')    
    
    def add(self, meal):
        """Add a MealCard object to the MealFolder.
        
        Args:
            meal (MealCard): The MealCard object to add to the MealFolder.

        Raises:
            TypeError: If the provided argument is not a MealCard object.
            ValueError: If a meal card with the same title already exists in the MealFolder.
        """
        if type(meal) != MealCard: raise TypeError('not a meal card')
        if meal.title.text in self.titles: raise ValueError('duplicate meal')
        self.titles.append(meal.title.text)
        self.mealcards.append(meal)
                
    def __iter__(self):
        """Return an iterator over the MealFolder's meal cards.
        
        Returns:
            iterator: An iterator over the meal cards stored in the MealFolder.
        """
        return iter(self.mealcards)

vegMealFolder = MealFolder()
vegMealFolder.add_all('vegetarian')

# Some checks
print(vegMealFolder.titles)

for m in vegMealFolder:
    print(m.title.text)

print(vegMealFolder.get_mealcard('Spanakopita').title.text)