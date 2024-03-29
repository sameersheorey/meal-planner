import os
from bs4 import BeautifulSoup
from MealCard import MealCard

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
            and add to the MealFolder object.
        
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

            new_mealcard = MealCard(mealdata)

            if filter is None:
                self.add(new_mealcard)

            elif new_mealcard.cats is not None and filter.casefold() in new_mealcard.cats.text.casefold():
                self.add(new_mealcard)
        
    def get_mealcard(self, title: str) -> MealCard:
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
    
    def add(self, meal: MealCard) -> None:
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