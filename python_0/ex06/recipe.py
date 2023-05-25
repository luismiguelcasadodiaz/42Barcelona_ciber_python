#!/usr/bin/python3

import sys
import os
"""
Part 1 Nested Dictionaries
Create a dictionary called cookbook.
"""
cookbook = {}
"""
You will use this cookbook to store recipe.
A recipe is a dictionary that stores (at least) 3 couples key-value:
• ”ingredients": a list of string representing the list of ingredients
• "meal": a string representing the type of meal
• "prep_time": a non-negative integer representing a time in minutes
In the cookbook, the key to a recipe is the recipe name.

Initialize your cookbook with 3 recipes:
• The Sandwich’s ingredients are ham, bread, cheese and tomatoes.
  It is a lunch and it takes 10 minutes of preparation.
"""
recipe = {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
        }
cookbook["Sandwich"] = recipe
"""
• The Cake’s ingredients are flour, sugar and eggs.
  It is a dessert and it takes 60 minutes of preparation.
"""
recipe = {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
        }
cookbook["cake"] = recipe

"""
• The Salad’s ingredients are avocado, arugula, tomatoes and spinach.
  It is a lunch and it takes 15 minutes of preparation.
"""
recipe = {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
        }
cookbook["salad"] = recipe

"""
Part 2 : A series of Helpful Functions
Create a series of useful functions to handle your cookbook:

1. A function that print all recipe names.
"""


def print_all():
    if cookbook != {}:
        for k in cookbook.keys():
            print_recipe(k)
    else:
        print("The cookbook is empty")


"""

2. A function that takes a recipe name and print its details.
"""


def print_recipe(name: str):
    print("Recipe for {}".format(name))
    print("\tIngredientes list: {}".format(cookbook[name]["ingredients"]))
    print("\tTo be eaten for {}.".format(cookbook[name]["meal"]))
    print("\tTakes {} minutes of cooking.".format(cookbook[name]["prep_time"]))
    print()


"""
3. A function that takes a recipe name and delete it.
"""


def delete_recipe(name: str):
    cookbook.pop(name)
    print("Recipe {} deleted".format(name))


"""
4. A function that add a recipe from user input.
    You will need a name, a list of ingredient,
    a meal type and a preparation time.
"""


def add_recipe():
    name = input("Enter a name:").strip()
    print("Enter ingredients (one per line. Ctrl-D to end)")
    raw_ingredients = sys.stdin.readlines()
    ingredients = [raw_ingredient.strip()
                   for raw_ingredient in raw_ingredients]
    meal = input("Ener a meal type:").strip()
    time = input("Enter a preparation time:").strip()
    recipe = {
            "ingredients": ingredients,
            "meal": meal,
            "prep_time": time,
            }
    cookbook[name] = recipe


# create a list of options to be displayes as a menu
menu_options = ["Add a recipe", "Delete a recipe",
                "Print a recipe", "Print the cookbook", "quit"]
num_options = len(menu_options)


def show_menu():
    os.system('clear')
    print("List of available option:")
    for num, text in enumerate(menu_options):
        print("\t{}: {}".format(num + 1, text))


def read_selection():
    correcto = False
    option = 0
    while not correcto:
        raw_option = input("Please select an option:")
        if raw_option.isnumeric():
            option = int(raw_option)
            if option <= num_options:
                correcto = True
            else:
                print("Option {} does not exist.".format(option))
        else:
            print("A letter is not an option.")
    return option


def read_recipe_name():
    recipe_name = ""
    good_name = False
    while not good_name:
        raw_recipe = input("Please enter a recipe name to get its details:")
        recipe_name = raw_recipe.strip()
        if recipe_name not in cookbook:
            print("Recipe {} does not exits".format(recipe_name))
        else:
            good_name = True
    return recipe_name


if __name__ == "__main__":
    quit = False
    while not quit:
        show_menu()
        option = read_selection()
        if option == 1:
            add_recipe()
        elif option == 2:
            delete_recipe(read_recipe_name())
        elif option == 3:
            print_recipe(read_recipe_name())
        elif option == 4:
            print_all()
        elif option == 5:
            quit = True
        option = input("Press Enter to continue") if not quit else None
    print("Cookbook closed. Goodbye !")
