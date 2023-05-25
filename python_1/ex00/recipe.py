#!/usr/bin/python3
"""
The Recipe class.

It has some attributes:
    • name (str): name of the recipe,
    • cooking_lvl (int): range from 1 to 5,
    • cooking_time (int): in minutes (no negative numbers),
    • ingredients (list): list of all ingredients each represented by a string,
    • description (str): description of the recipe,
    • recipe_type (str): can be "starter", "lunch" or "dessert".
"""

import string


class Recipe:
    __TYPE = ["starter", "lunch", "dessert"]
    __MIN_LVL = 1
    __MAX_LVL = 5

    def __init__(self,
                 n: str,     # name of the recipe,
                 c_l: int,      # range from MIN_LVL to MAX_LVL
                 c_t: int,      # in minutes (no negative numbers)
                 ingre: list,   # ingredients' list. One string per ingredient
                 desc: str,     # description of the recipe,
                 r_type: str    # can be "starter", "lunch" or "dessert"
                 ):
        self.name = n
        self.cooking_lvl = c_l
        self.cooking_time = c_t
        self.ingredients = ingre
        self.description = desc
        self.recipe_type = r_type

    # I protect class attributes from beting settle incorrectly

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        thename = ""
        for char in value:
            if char in string.ascii_letters or char == " ":
                thename = thename + char
            else:
                raise ValueError("Recipe name accepts only letters and spaces")
        self._name = thename

    @property
    def cooking_lvl(self) -> int:
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, value: int):
        if isinstance(value, int) and \
           self.__MIN_LVL <= value and value <= self.__MAX_LVL:
            self._cooking_lvl = value
        else:
            msg = f"Recipe level out of range: \
                {self.__MIN_LVL}..{self.__MAX_LVL}"
            raise ValueError(msg)

    @property
    def cooking_time(self) -> int:
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, value: int):
        if value > 0:
            self._cooking_time = value
        else:
            raise ValueError("cooking time must a non-zero positive nmber")

    @property
    def ingredients(self) -> list:
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value: list):
        if isinstance(value, list) and value != []:
            self._ingredients = value
        else:
            raise ValueError("Non list type or empty used to set ingredients")

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        for char in value:
            if char in string.printable:
                self._description = value
            else:
                msg = "Only printable chars allowed in descrition"
                raise ValueError(msg)

    @property
    def recipe_type(self) -> str:
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, value):
        if value in self.__TYPE:
            self._recipe_type = value
        else:
            raise ValueError(f" {value} not in {self.__TYPE}")

    # function to prin
    def __str__(self):
        """Return the string to print with the recipe info"""
        line1 = f"Recipe name : {self._name}\n"
        line2 = f"Recipe level: {self._cooking_lvl}\n"
        line3 = f"Cooking time: {self._cooking_time}\n"
        line4 = f"Ingredients :\n"
        for i in self._ingredients:
            line4 = line4 + f"\t{i}\n"
        line5 = f"Instructions:\n\t{self._description}\n"
        line6 = f"Recipe type : {self._recipe_type}\n"
        txt = line1 + \
            line2 + \
            line6 + \
            line3 + \
            line4 + \
            line5
        return txt

        def __repr__(self):
            return f"Recipe {self.name} his made of {self.ingredients}"


if __name__ == '__main__':
    recipe2 = Recipe("tortilla", 3, 45,
                     ["patatas", "huevos", "aceite", "sal"],
                     "pelar, batir, mezclar freir", "lunch")
    print(recipe2)
