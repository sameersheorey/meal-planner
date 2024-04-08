class MealCard:
    """A class to represent a single meal card.

    Attributes:
        meal_id (int): The ID of the meal.
        title (str): The title of the meal.
        rating (str): The rating of the meal.
        metadata (str): Additional metadata of the meal.
        cats (str): Categories of the meal.
        ingredients (list[str]): List of ingredients for the meal.
    """
    def __init__(self, meal_id: int, title: str, rating: str, 
                 metadata: str, cats: str, 
                 ingredients: list[str]) -> None:
        """Initialize the MealCard object."""
        
        self.id = meal_id
        self.title = title
        self.rating = rating
        self.metadata = metadata
        self.cats = cats
        self.ingredients = ingredients