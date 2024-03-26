# Create an ingredients list for the week


def SimpleIngredientsGenerator(menu):
    new_ingredients = []
    for day in menu.keys():
        for ingredient in menu[day]['ingredients']:
            # print(ingredient.text)
            new_ingredients.append(ingredient.text)
    return new_ingredients