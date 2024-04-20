class MenuItem:
    """A class to represent a single meal card.

    Attributes:
        menu_id (int): The ID of the menu.
        date (str): The date of the menu item.
        meal_id (int): The ID of the meal.
        added_to_shopping: int: 0 if the meal is not added to the shopping list, 1 if it is.
    """
    
    def __init__(self, menu_id: int, date: str, meal_id: int, added_to_shopping: int) -> None:
        """Initialize the Menu object with a menu_id, date and title."""
        
        self.menu_id = menu_id
        self.date = date
        self.meal_id = meal_id
        self.added_to_shopping = added_to_shopping