class MealCard:
    """A class to represent a single meal card.

    Attributes:
        title (BeautifulSoup.Tag): The title of the meal.
        rating (BeautifulSoup.Tag): The rating of the meal.
        metadata (BeautifulSoup.Tag): Additional metadata of the meal.
        cats (BeautifulSoup.Tag): Categories of the meal.
        ingredients (list): List of ingredients for the meal.
    """
    
    def __init__(self, mealdata):
        """Initialize the MealCard object with data from a meal HMTL file.
        
        Args:
            mealdata: BeautifulSoup object representing the HTML content of a meal HTML file.
        """
        
        self.title = mealdata.find('h1')
        self.rating = mealdata.find('p', class_="rating")
        self.metadata = mealdata.find('p', class_="metadata")
        self.cats = mealdata.find('p', class_="categories")
        self.ingredients = mealdata.find_all('p', itemprop="recipeIngredient")