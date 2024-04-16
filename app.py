from flask import Flask, render_template, redirect, url_for
from dbMealFolder import dbMealFolder
from dbMenu import dbMenu
from dbShoppingList import dbShoppingList
from dbStoreCupboard import dbStoreCupboard
from flask import request
from utils import *

app = Flask(__name__)

veg_meals = dbMealFolder()
menu = dbMenu()
shopping_list = dbShoppingList('shopping_list.db')
store_cupboard = dbStoreCupboard('store_cupboard.db')

# Dummy items added to stock cupboard - note will add items twice in debug mode TODO: workaround for this
store_cupboard.add_ingredients(store_cupboard_dummy)

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
    menu_items = menu.get_menu(order_by_date=True)
    meals = []
    dates = []

    for item in menu_items:
        meal = veg_meals.get_meal_by_id(item.meal_id)
        meals.append(meal)
        dates.append(item.date)
    
    formatted_date = [change_date_format(date) for date in dates]

    menu_display = zip(menu_items, meals, formatted_date)
    return render_template('menu.html', menu_display = menu_display, dates = dates)


@app.route("/add_menu_item", methods=['POST'])
def add_menu_item():
    meals = veg_meals.get_all_meals()

    selected_start_date = request.form.get('startDate')
    selected_end_date = request.form.get('endDate')
    
    dates = get_dates_in_between(selected_start_date, selected_end_date )
    
    for date in dates:
        if menu.date_in_menu(date):
            pass
        # TODO: if date already exists in database, ask user if they want to replace it. If yes, replace it, if no, skip it
        else:
            menu.add_random_meal(meals, date)
    
    return redirect(url_for('display_menu'))


@app.route("/delete_menu_item/<menu_id>", methods=['POST'])
def delete_menu_item(menu_id):
    shopping_list.delete_ingredients_by_menu_id(menu_id)
    menu.delete_menu_item_by_menu_id(menu_id)
    return redirect(url_for('display_menu'))


@app.route("/replace_menu_item/<menu_id>", methods=['POST'])
def replace_menu_item(menu_id):
    shopping_list.delete_ingredients_by_menu_id(menu_id)
    meals = veg_meals.get_all_meals()
    menu.replace_menu_item(meals, menu_id)
    return redirect(url_for('display_menu'))


@app.route("/add_to_shopping/<menu_id>/<meal_id>", methods=['POST'])
def add_to_shopping(menu_id, meal_id):
    new_ingredients = veg_meals.get_meal_by_id(meal_id).ingredients
    store_comparison_dict = store_cupboard.find_similar_ingredients(new_ingredients)
    
    for sublist in store_comparison_dict.values():
        for item in sublist:
            if item in new_ingredients:
                new_ingredients.remove(item)

    shopping_list.add_ingredients(new_ingredients, menu_id)
    menu.toggle_added_to_shopping(menu_id)
    return render_template('store_comparison.html', store_comparison_dict = store_comparison_dict, menu_id = menu_id)


@app.route("/add_to_shopping/compared_ingredients/<menu_id>", methods=['POST'])
def add_compared_ingredients_to_shopping(menu_id):
    add_anyway_ingredients = request.form.getlist("add_anyway")
    add_anyway_ingredients = unpack_lists(add_anyway_ingredients)

    custom_ingredients = request.form.getlist("customIngredient")
    custom_ingredients = [ingredient for ingredient in custom_ingredients if ingredient.strip()]

    ingredients_to_add = add_anyway_ingredients + custom_ingredients

    shopping_list.add_ingredients(ingredients_to_add, menu_id)
    return redirect(url_for('display_menu'))


@app.route("/delete_from_shopping/<menu_id>", methods=['POST'])
def delete_from_shopping(menu_id):
    shopping_list.delete_ingredients_by_menu_id(menu_id)
    menu.toggle_added_to_shopping(menu_id)
    return redirect(url_for('display_menu'))


@app.route("/shopping_list")
def display_shopping_list():
    ingredients = shopping_list.get_ingredients_list()
    return render_template('shopping_list.html', ingredients = ingredients)


@app.route("/store_cupboard")
def display_store_cupboard():
    ingredients = store_cupboard.get_ingredients()
    return render_template('store_cupboard.html', ingredients = ingredients)


@app.route("/add_store_cupboard_item", methods=['POST'])
def add_store_cupboard_item():
    ingredient = request.form.getlist("add_ingredient")
    print(ingredient)
    store_cupboard.add_ingredients(ingredient)
    return redirect(url_for('display_store_cupboard'))


@app.route("/delete_store_cupboard_items", methods=['POST'])
def delete_store_cupboard_items():
    ingredient_ids = request.form.getlist("delete_ingredients")
    print(ingredient_ids)
    for id in ingredient_ids:
        store_cupboard.delete_ingredients_by_id(id)
    return redirect(url_for('display_store_cupboard'))


@app.route('/<filename>')
def serve_html(filename):
    return render_template(f'saved_meals/{filename}.html')


if __name__ == '__main__':
    app.run(debug=True)


