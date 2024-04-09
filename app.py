from flask import Flask, render_template, redirect, url_for
from dbMealFolder import dbMealFolder
from dbMenu import dbMenu
from dbShoppingList import dbShoppingList
from dbStockCupboard import dbStockCupboard

app = Flask(__name__)

veg_meals = dbMealFolder()
menu = dbMenu()
shopping_list = dbShoppingList('shopping_list.db')
stock_cupboard = dbStockCupboard('stock_cupboard.db')

# Dummy items added to stock cupboard - note will add items twice in debug mode TODO: workaround for this
stock_cupboard.add_ingredients(['dummy 1', 'dummy 2', 'dummy 3'])
# print('hello')

@app.route("/")
def display_all_meals():
    meals = veg_meals.get_all_meals()
    return render_template('home.html', meals = meals)


@app.route("/add_vegetarian_meals", methods=['POST'])
def add_vegetarian_meals():
    veg_meals.add_all("vegetarian")
    return redirect(url_for('display_all_meals'))


@app.route("/menu")
def display_menu():
    menu_items = menu.get_menu()
    meals = []
    for item in menu_items:
        meal = veg_meals.get_meal_by_id(item.meal_id)
        meals.append(meal)
    
    menu_display = zip(menu_items, meals)
    return render_template('menu.html', menu_display = menu_display)


@app.route("/add_menu_item", methods=['POST'])
def add_menu_item():
    meals = veg_meals.get_all_meals()
    menu.add_random_meal(meals)
    new_meal = menu.get_menu()[-1]
    new_ingredients = veg_meals.get_meal_by_id(new_meal.meal_id).ingredients
    shopping_list.add_ingredients(new_ingredients, new_meal.menu_id)
    return redirect(url_for('display_menu'))


@app.route("/delete_menu_item/<menu_id>", methods=['POST'])
def delete_menu_item(menu_id):
    shopping_list.delete_ingredients_by_menu_id(menu_id)
    menu.delete_menu_item_by_menu_id(menu_id)
    return redirect(url_for('display_menu'))


@app.route("/shopping_list")
def display_shopping_list():
    ingredients = shopping_list.get_ingredients_list()
    return render_template('shopping_list.html', ingredients = ingredients)


@app.route("/stock_cupboard")
def display_stock_cupboard():
    ingredients = stock_cupboard.get_ingredients_list()
    return render_template('stock_cupboard.html', ingredients = ingredients)


@app.route('/<filename>')
def serve_html(filename):
    return render_template(f'saved_meals/{filename}.html')


if __name__ == '__main__':
    app.run(debug=True)


