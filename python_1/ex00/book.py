#!/usr/bin/python3
"""
The Book class.

The Book class also has some attributes:
• name (str): name of the book,
• last_update (datetime): the date of the last update,
• creation_date (datetime): the creation date,
• recipes_list (dict): a dictionnary with 3 keys:
"starter", "lunch", "dessert".

"""
from datetime import datetime
import copy


class Book:
    __empty_recipes_list = {"starter": [],
                            "lunch": [],
                            "dessert": []}
    __now = datetime.today()

    def __init__(self, name: str):
        self.name = name
        # self.recipes = self.__empty_recipes_list
        self.recipes = copy.deepcopy(self.__empty_recipes_list)
        self.last_update = None  # at creation time there is not update
        self.creation_date = self.set_creation_date()

    def set_creation_date(self):
        return datetime.today()

    def set_last_update(self):
        self.last_update = self.set_creation_date()
        return

    def get_recipe_by_name(self, name=None):
        """
        Prints a recipe with the name \texttt{name}
        and returns the instance
        """
        found = False
        the_recipe = None
        for arecipe in self:
            if name == arecipe.name:
                found = True
                the_recipe = arecipe
        if found:
            print(the_recipe)
            return the_recipe
        else:
            print(f"\texttt {name} not found in {self.name}")

    def get_recipes_by_types(self, recipe_type=""):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in self.recipes:
            print(f"{recipe_type} is not a validad recipe type")
        else:
            return self.recipes[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if recipe.name not in self:
            self.recipes[recipe.recipe_type].append(recipe)
            print(f"Recipe {recipe.name} added as {recipe.recipe_type}")
            self.last_update = self.set_creation_date()
        else:
            print(f"The book already has a {recipe.name}")

    def print_all(self):
        print(f"recipes in {self.name}")
        print("="*40)
        for k in self:
            print(str(k))
        print("="*40)

    def __iter__(self):
        all_recipes = []
        for key in self.recipes.keys():
            key_list = self.get_recipes_by_types(key)
            for arecipe in key_list:
                all_recipes.append(arecipe)
        for recipe in all_recipes:
            yield recipe

    def __contains__(self, onename):
        exist = False
        for recipe in self:
            if recipe.name == onename:
                exist = True
        return exist
