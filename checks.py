from MealFolderTesting import MealFolder

vegMealFolder = MealFolder()
vegMealFolder.add_all('vegetarian')


# Some more checks

print(vegMealFolder.mealcards[1].ingredients)


