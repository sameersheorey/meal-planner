class IngredientItem:
    """A class to represent an ingredient item for a meal.

    Attributes:
        id (int): The unique identifier of the ingredient item.
        ingredient (str): The name of the ingredient.
        menu_id (int): The ID of the menu this ingredient belongs to.
    """
    
    def __init__(self, id: int, ingredient: str, menu_id: int) -> None:
        """Initialize the IngredientItem object with an ID, ingredient name, and menu ID."""
        
        self.id = id
        self.ingredient = ingredient
        self.menu_id = menu_id
        