import random

class Menu:
    """A class to manage weekly menus.

    Attributes:
        menus (list): A list to store weekly menus.
        ingredients (list): A list to store weekly ingredients.
    """
        
    def __init__(self):
        """Initialize a Menu object.
        
        Creates an empty list to store weekly menus and an empty list to store weekly ingredients.
        """
        self.menus = []
        self.ingredients = []

    def add_menu(self, MealFolder, menu_generator="random"):
        """Add a menu to the list of weekly menus and the ingredients from that menus to
            the list of weekly ingredients
        
        Args:
            MealFolder (MealFolder): The MealFolder object from which to generate the menu.
            menu_generator (str, optional): The type of menu generator to use. Defaults to "random".
        """
        if menu_generator == "random":
            menu = self.RandomMenuGenerator(MealFolder)

        self.menus.append(menu)
        self.ingredients.append(self.IngredientsGenerator(menu)) 
    
    def replace_menu(self, MealFolder, menu_generator="random"):
        """Replace the latest menu in the list of weekly menus with a newly generated menu.
        
        Args:
            MealFolder (MealFolder): The MealFolder object from which to generate the menu.
            menu_generator (str, optional): The type of menu generator to use. Defaults to "random".
        """
        if menu_generator == "random":
            self.menus[-1] = self.RandomMenuGenerator(MealFolder)

    def RandomMenuGenerator(self, MealFolder):
        """Generate a random weekly menu from the given MealFolder.
        
        Args:
            MealFolder (MealFolder): The MealFolder object to generate the menu from.
        
        Returns:
            dict: A dictionary representing the weekly menu, with days as keys and meal titles as values.
        """
        
        menu = {}
        days = ['M', 'Tu','W', 'Th', 'F', 'Sa', 'Su']

        for day in days: 
            menu[day] = random.choice(MealFolder.mealcards)
        
        return menu

    def IngredientsGenerator(self, menu):
        """Generate a list of ingredients from a given menu.
        
        Args:
            menu (dict): A dictionary representing the menu, with days as keys and meal information as values.

        Returns:
            list: A list of ingredients extracted from the menu.
        """

        new_ingredients = []

        for day in menu.keys():
            for ingredient in menu[day].ingredients:
                new_ingredients.append(ingredient.text)
        return new_ingredients