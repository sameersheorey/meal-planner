from MealFolder import *
from Menu import *

vegMealFolder = MealFolder()
vegMealFolder.add_all('vegetarian')

menulist = Menu()
# print(menulist.menu_titles)

menulist.add_menu(vegMealFolder, 'random')
# print(menulist.menu_titles)

menulist.add_menu(vegMealFolder, 'random')
# print(menulist.menu_titles)

menulist.replace_menu(vegMealFolder, 'random')
# print(menulist.menu_titles)

print(menulist.menu_titles[-1])
# print(menulist.ingredients[-1])

# Some more checks

# print(vegMealFolder.titles)

# for m in vegMealFolder:
#     print(m.title.text)

# print(vegMealFolder.get_mealcard('Spanakopita').title.text)

# print(random.choice(vegMealFolder.mealcards).title.text)