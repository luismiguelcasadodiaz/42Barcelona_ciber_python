#!/usr/bin/python3
from recipe import Recipe
from book import Book
import os
import sys


def add_recipe():
    name = input("Enter a name:").strip()
    print("Enter ingredients (one per line. Ctrl-D to end)")
    raw_ingredients = sys.stdin.readlines()
    ingredients = [raw_ingredient.strip()
                   for raw_ingredient in raw_ingredients]
    meal = read_meal_type()
    level = read_recipe_level()
    time = read_cooking_time()
    inst = input("Explain how to cook: ").strip()
    the_recipe = Recipe(name, level, time, ingredients, inst, meal)
    cookbook.add_recipe(the_recipe)


# create a list of options to be displayes as a menu
menu_options = ["Add a recipe", "Delete a recipe",
                "Print a recipe", "Print the cookbook", "quit"]
num_options = len(menu_options)


def read_recipe_level():
    correcto = False
    option = 0
    while not correcto:
        raw_option = input("Enter recipe level:")
        if raw_option.isnumeric():
            option = int(raw_option)
            if 1 <= option <= 5:
                correcto = True
            else:
                print("Option {} does not exist.".format(option))
        else:
            print("A letter is not an option.")
    return option


def read_cooking_time():
    correcto = False
    option = 0
    while not correcto:
        raw_option = input("Enter a preparation time:")
        if raw_option.isnumeric():
            option = int(raw_option)
            if 0 < option:
                correcto = True
            else:
                print("Preparation time must be positive")
        else:
            print("A letter is not a good preparation time.")
    return option


def show_menu():
    os.system('clear')
    print("List of available option:")
    for num, text in enumerate(menu_options):
        print("\t{}: {}".format(num + 1, text))


def read_meal_type():
    correcto = False
    while not correcto:
        raw_option = input("Enter a meal type:")
        if raw_option in ["starter", "lunch", "dessert"]:
            correcto = True
        else:
            print(f"Incorrect meal type {raw_option} does not exist.")
    return raw_option


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
    cookbook = Book("Luis")
    recipe1 = Recipe("tortilla", 3, 45,
                     ["patatas", "huevos", "aceite", "sal"],
                     "pelar, batir, mezclar freir", "lunch")
    recipe2 = Recipe("sandwich", 2, 30,
                     ["ham", "bread", "cheese", "tomatoes"],
                     "cortar untar colocar", "lunch")
    recipe3 = Recipe("cake", 4, 60,
                     ["flour", "sugar", "eggs"],
                     "mezclar todo", "dessert")
    recipe4 = Recipe("salad", 2, 15,
                     ["avocado", "arugula", "tomatoes", "spinach"],
                     "Alinyar", "lunch")
    cookbook.add_recipe(recipe1)
    cookbook.add_recipe(recipe2)
    cookbook.add_recipe(recipe3)
    cookbook.add_recipe(recipe4)

    quit = False
    while not quit:
        show_menu()
        option = read_selection()
        if option == 1:
            add_recipe()
        elif option == 2:
            delete_recipe(read_recipe_name())
        elif option == 3:
            cookbook.get_recipe_by_name(read_recipe_name())
        elif option == 4:
            cookbook.print_all()
        elif option == 5:
            quit = True
        option = input("Press Enter to continue") if not quit else None
    print("Cookbook closed. Goodbye !")
