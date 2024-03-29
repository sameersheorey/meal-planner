import random
import MealFolder

class Menu:
    """A class to manage weekly menus.

    Attributes:
        menus (list): A list to store weekly menus.
        menu_titles (list): A list to store weekly menu titles.
        ingredients (list): A list to store weekly ingredients.
    """
        
    def __init__(self):
        """Initialize a Menu object.
        
        Creates an empty list to store weekly menus and an empty list to store weekly ingredients.
        """
        self.menus = []
        self.menu_titles = []
        self.ingredients = []

    def add_menu(self, MealFolder: MealFolder, menu_generator: str = "random") -> None:
        """Add a menu to the list of weekly menus, the menu titles to the list of weekly menu titles
          and the ingredients from that menus to the list of weekly ingredients
        
        Args:
            MealFolder (MealFolder): The MealFolder object from which to generate the menu.
            menu_generator (str, optional): The type of menu generator to use. Defaults to "random".
        """
        if menu_generator == "random":
            menu, titles, ingredients = self.RandomMenuGenerator(MealFolder)

        self.menus.append(menu)
        self.menu_titles.append(titles)
        self.ingredients.append(ingredients) 
    
    def replace_menu(self, MealFolder: MealFolder, menu_generator: str ="random") -> None:
        """Replace the latest weekly menu, weekly menu titles and weekly ingredients in 
            their respeecive lists with those of a newly generated menu.
        
        Args:
            MealFolder (MealFolder): The MealFolder object from which to generate the menu.
            menu_generator (str, optional): The type of menu generator to use. Defaults to "random".
        """
        if menu_generator == "random":
            menu, titles, ingredients = self.RandomMenuGenerator(MealFolder)

        self.menus[-1] = menu
        self.menu_titles[-1]= titles
        self.ingredients[-1] = ingredients

    def RandomMenuGenerator(self, MealFolder: MealFolder) -> dict:
        """Generate a random weekly menu from the given MealFolder.
        
        Args:
            MealFolder (MealFolder): The MealFolder object to generate the menu from.
        
        Returns:
            dict: A dictionary representing the weekly menu, with days as keys and meal cards as values.
            dict: A dictionary with the weekly menu titles, with days as keys and meal titles as values.
            list: A list of ingredients extracted from the menu.
        """
        
        menu = {}
        titles = {}
        new_ingredients = []
        days = ['M', 'Tu','W', 'Th', 'F', 'Sa', 'Su']

        for day in days:
            menu[day] = random.choice(MealFolder.mealcards)
            titles[day] = menu[day].title.text

            for ingredient in menu[day].ingredients:
                new_ingredients.append(ingredient.text)
        
        return menu, titles, new_ingredients