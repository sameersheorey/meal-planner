import numpy as np
import os
import random
# import html5lib
from bs4 import BeautifulSoup

# Open the HTML file
mealList = []

for file in os.listdir('mealData'):
    filename = os.fsdecode(file)
    # print(filename)
    if filename == '.DS_Store':
        continue

    with open(f'mealData/{filename}', 'r', encoding='utf-8') as file:
        # Read the contents of the file
        html_content = file.read()

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')
        #print(soup)

        # Extract data based on HTML tags, attributes, etc.
        # Example: Extracting all text from paragraph tags
        # paragraphs = soup.find_all('p')
        # for paragraph in paragraphs:
        #     print(paragraph.get_text())

        # Example: Extract meal title
        titles = soup.find_all('h1')
        for title in titles:
            mealList.append(title.get_text())

meals = {}
for i in range(1,7):
    meals[i] = random.choice(mealList)

print(meals)
      