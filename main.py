from MealFolder import MealFolder
from Menu import Menu


vegMealFolder = MealFolder()
vegMealFolder.add_all('vegetarian')

menulist = Menu()

menulist.add_menu(vegMealFolder, 'random')

menulist.add_menu(vegMealFolder, 'random')

menulist.replace_menu(vegMealFolder, 'random')

print(menulist.menu_titles[-1])

# Some more checks

print(vegMealFolder.titles)

for m in vegMealFolder:
    print(m.title.text)

print(vegMealFolder.get_mealcard('Spanakopita').title.text)

