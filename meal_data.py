import numpy as np
import os
import random
from bs4 import BeautifulSoup

meals = {}

# Open the HTML file
for idx, file in enumerate(os.listdir('mealData')):
    mealAttributes = {}
    # print(idx)
    filename = os.fsdecode(file)
    # print(filename)
    if filename == '.DS_Store':
        continue

    with open(f'mealData/{filename}', 'r', encoding='utf-8') as file:
        # Read the contents of the file
        html_content = file.read()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract meal title
    title = soup.find('h1')
    mealAttributes['title'] = title

    # Extract rating
    rating = soup.find('p', class_="rating")
    mealAttributes['rating'] = rating['value']

    # Extract metadata (prep time, cook time, total time, servings)
    metadata = soup.find('p', class_="metadata")
    mealAttributes['metadata'] = metadata

    # Extract meal categories
    cats = soup.find('p', class_="categories")
    mealAttributes['categories'] = cats
    
    # Extract meal ingredients
    ingredients = soup.find_all('p', itemprop="recipeIngredient")
    for ingredient in ingredients:
        mealAttributes['ingredients'] = ingredients

    meals[idx] = mealAttributes

# Filter meals to vegetarian only

vegMeals = {}

i=0
for mealAttributes in meals.values():
    if mealAttributes['categories'] is not None and 'vegetarian'.casefold() in mealAttributes['categories'].text.casefold():
            vegMeals[i] = mealAttributes
            i += 1

# Create a random menu for the week out of the veg meals

menu = {}
days = ['M', 'Tu','W', 'Th', 'F', 'Sa', 'Su']

for day in days: 
    menu[day] = random.choice(vegMeals)
    
for day in menu.keys():
     print(f"{day}: {menu[day]['title'].text}")

# Create an ingredients list for the week
     
new_ingredients = []
for day in menu.keys():
    for ingredient in menu[day]['ingredients']:
        print(ingredient.text)
        new_ingredients.append(ingredient.text)

print(new_ingredients)