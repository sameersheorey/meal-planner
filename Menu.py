class Menu:
    """A class to represent a single meal card.

    Attributes:
        date (str): The date of the meal.
        title (str): The title of the meal.
    """
    
    def __init__(self, date: str, title: str) -> None:
        """Initialize the Menu object with a date and title."""
        
        self.date = date
        self.title = title