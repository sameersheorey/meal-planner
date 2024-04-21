import re

class IngredientItem:
    """A class to represent an ingredient item for a meal.

    Attributes:
        id (int): The unique identifier of the ingredient item.
        ingredient (str): The name of the ingredient.
        menu_id (int): The ID of the menu this ingredient belongs to.
    """
    
    def __init__(self, id: int, ingredient: str, menu_id: int) -> None:
        """Initialize the IngredientItem object with an ID, menu ID, ingredient amount, ingredient unit and ingredient"""
        
        self.id = id
        self.ingredient = ingredient
        self.menu_id = menu_id
        self._get_amount()
        self._get_unit()


    def _get_amount(self) -> None:
        """Finds numeric values at start of ingredient, sets as amount attribute and removes from ingredient attribute"""
        amount_regex = '[0-9]+(.[0-9]*)?'
        amount_match = re.match(amount_regex, self.ingredient)
        if amount_match:
            amount_span = amount_match.span()
            self.amount = self.ingredient[amount_span[0]: amount_span[1]]
            self.ingredient = self.ingredient[amount_span[1]:].strip()
        else:
            self.amount = None
    
    def _get_unit(self) -> None:
        """Finds unit values at start of ingredient, sets as unit attribute and removes from ingredient attribute"""
        unit_regex = '(ml |g |tsp |tbsp |litres |tin )'
        unit_match = re.match(unit_regex, self.ingredient)
        if unit_match:
            unit_span = unit_match.span()
            self.unit = self.ingredient[unit_span[0]: unit_span[1]].strip()
            self.ingredient = self.ingredient[unit_span[1]:].strip()
        else:
            self.unit = None