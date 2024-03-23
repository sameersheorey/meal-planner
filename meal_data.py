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
    
# for day in menu.keys():
#      print(f"{day}: {menu[day]['title'].text}")

# Create an ingredients list for the week
     
new_ingredients = []
for day in menu.keys():
    for ingredient in menu[day]['ingredients']:
        # print(ingredient.text)
        new_ingredients.append(ingredient.text)

# print(new_ingredients)

# Compare to stock cupboard

# create dummy stock cupboard

stock_cupboard = ['For the pasta and sauce:', '1 tbsp olive oil', '1 brown onion, finely chopped', 
                  '2 cloves garlic, finely chopped (or 1 cube frozen garlic)', '1/2 tsp chilli flakes', 
                  '500g passata', '4 cubes of frozen spinach', '1/2 tsp salt', '250g dried pasta', 
                  '125g whole-milk ricotta cheese', '25g grated Parmesan cheese', '110g shredded mozzarella cheese', 
                  '1 box lasagne sheets', '1 large onion, chopped', '3 cloves garlic, crushed', '1 tsp. dried oregano', 
                  '2 cans tomatoes', '10 mushrooms', '2 peppers', '4 carrots', 
                  "x spinach, (can use frozen spinach that's been thawed and drained of excess liquid)", 
                  'x g cheddar (grated)', '500ml milk', '1/2 tsp. ground cinnamon', 'x parmesan', '350 g mozzarella (optional)', 
                  '280g/10oz cherry tomatoes on the vine', '1 tbsp olive oil', '1.2 tbsp balsamic vinegar', '500g/1.1 lb gnocchi', 
                  '3 tbsp butter', '2 cloves garlic', '90g/3.3oz spinach', '2 tbsp chopped basil', 
                  '1/4 tsp cracked black pepper plus more for serving', '1/4 tsp sea salt plus more for serving', 
                  '210g Mozzarella cheese', '25g/2 tbsp pine nuts', 'For the batter:', '100g plain flour', '2 eggs', 
                  '150ml semi-skimmed milk', 'For the toad:', '8 pork sausages (or swap in some veggie)', '1 onion, finely sliced', 
                  '1 tbsp vegetable oil', 'For the gravy:', '1 onion, finely sliced', '1 tbsp vegetable oil', '2 tsp plain flour', 
                  '2 tsp English mustard', '2 tsp Worcestershire sauce', '1 vegetable stock cube, made up to 300ml', 
                  '1 cauliflower - cut into florets ', 'Chicken breast (optional)', 'olive oil', 'sea salt', 'freshly cracked black pepper', 
                  '2 tbsp  soy sauce', '2 tbsp hoisin sauce', '2 tbsp red wine vinegar', '1 tbsp toasted sesame oil', '2 tsp brown sugar',
                  '2 tsp cornflour', '2 garlic cloves, minced', '2 tsp freshly grated ginger', '1 tsp chilli flakes', '50g peanuts, chopped', 
                  '4 spring onions, thinly sliced', 'jasmine rice, for serving', '320g pack ready-rolled puff pastry', '2 tsp milk', '1 leek', 
                  '1 large roasted beetroot', '4 tbsp soft cheese', '200g goat cheese', '16g Marmite', '50g agave nectar', '2 tsp cornflour', 
                  '30ml mirin', '560g tofu', '100g roasted peanuts', '60ml soy sauce']

# create list of ingredients already in stock_cupboard

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_similar_ingredients(stock_cupboard, new_ingredients, similarity_threshold = 0.7):
    stock_comparison = {}
    for stock_item in stock_cupboard:
        similar_items = []
        for menu_item in new_ingredients:
            similarity = similar(stock_item, menu_item)
        if similarity > similarity_threshold:
            similar_items.append(menu_item)
        if similar_items:
            stock_comparison[stock_item] = similar_items
    return stock_comparison

stock_comparison = find_similar_ingredients(stock_cupboard, new_ingredients, similarity_threshold = 0.7)

print(stock_comparison)