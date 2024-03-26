from MealFolder import *
from Menu import *


vegMealFolder = MealFolder()
vegMealFolder.add_all('vegetarian')

menulist = Menu()
# print(menulist.menus)
menulist.add_menu(vegMealFolder, 'random')
# print(menulist.menus)
menulist.add_menu(vegMealFolder, 'random')
# print(menulist.menus)


print(menulist.ingredients[-1])

# Some checks

# print(vegMealFolder.titles)

# for m in vegMealFolder:
#     print(m.title.text)

# print(vegMealFolder.get_mealcard('Spanakopita').title.text)

# print(random.choice(vegMealFolder.mealcards).title.text)