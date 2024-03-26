import os
from bs4 import BeautifulSoup

class MealCard:
     def __init__(self, mealdata):
        self.title = mealdata.find('h1')
        self.rating = mealdata.find('p', class_="rating")
        self.metadata = mealdata.find('p', class_="metadata")
        self.cats = mealdata.find('p', class_="categories")
        self.ingredients = mealdata.find_all('p', itemprop="recipeIngredient")


class MealFolder:
    def __init__(self):
        self.titles = []
        self.mealcards = []
        
    def add_all(self, filter = None):
        for file in os.listdir('mealData'):
            # Open the HTML files
            filename = os.fsdecode(file)
            # print(filename)
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
        for meal_card in self:
            if meal_card.title.text == title:
                return meal_card
        raise ValueError(f'Meal with title "{title}" not found')    
    
    def add(self, meal):
        if type(meal) != MealCard: raise TypeError('not a meal card')
        if meal.title.text in self.titles: raise ValueError('duplicate meal')
        self.titles.append(meal.title.text)
        self.mealcards.append(meal)
                
    def __iter__(self):
        return iter(self.mealcards)

vegMealFolder = MealFolder()
vegMealFolder.add_all('vegetarian')

# Some checks
print(vegMealFolder.titles)

for m in vegMealFolder:
    print(m.title.text)

print(vegMealFolder.get_mealcard('Spanakopita').title.text)