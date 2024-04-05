from flask import Flask, render_template, redirect, url_for
from dbMealFolder import dbMealFolder
from dbMenu import dbMenu

app = Flask(__name__)

veg_meals = dbMealFolder()
menu = dbMenu()

@app.route("/")
def display_all_meals():
    display_meals = veg_meals.get_all_meals()
    return render_template('home.html', meals = display_meals)

@app.route("/add_vegetarian_meals", methods=['POST'])
def add_vegetarian_meals():
    veg_meals.add_all("vegetarian")
    return redirect(url_for('display_all_meals'))

@app.route("/menu")
def display_menu():
    display_menu = menu.get_menu()
    return render_template('menu.html', menu = display_menu)

@app.route("/add_menu_item", methods=['POST'])
def add_menu_item():
    meals = veg_meals.get_all_meals()
    menu.add_random_meal(meals)
    return redirect(url_for('display_menu'))

@app.route('/<filename>')
def serve_html(filename):
    return render_template(f'saved_meals/{filename}.html')

if __name__ == '__main__':
    app.run(debug=True)


