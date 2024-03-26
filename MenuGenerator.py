import random

def RandomMenuGenerator(MealFolder):
    menu = {}
    days = ['M', 'Tu','W', 'Th', 'F', 'Sa', 'Su']

    for day in days: 
        menu[day] = random.choice(MealFolder)
    
    return menu