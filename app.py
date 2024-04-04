from flask import Flask, render_template
from dbMealFolder import dbMealFolder

app = Flask(__name__)


@app.route("/")
def display_all_meals():
    veg_meals = dbMealFolder()
    veg_meals.add_all("vegetarian")
    display_meals = veg_meals.get_all_meals()
    return render_template('home.html', meals = display_meals)

@app.route('/<filename>')
def serve_html(filename):
    return render_template(f'saved_meals/{filename}.html')

if __name__ == '__main__':
    app.run(debug=True)


