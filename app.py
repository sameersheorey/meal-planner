from flask import Flask, render_template, redirect, url_for
from dbMealFolder import dbMealFolder

app = Flask(__name__)

veg_meals = dbMealFolder()

@app.route("/")
def display_all_meals():
    display_meals = veg_meals.get_all_meals()
    return render_template('home.html', meals = display_meals)

@app.route("/add_vegetarian_meals", methods=['POST'])
def add_vegetarian_meals():
    veg_meals.add_all("vegetarian")
    return redirect(url_for('display_all_meals'))

@app.route('/<filename>')
def serve_html(filename):
    return render_template(f'saved_meals/{filename}.html')

if __name__ == '__main__':
    app.run(debug=True)


