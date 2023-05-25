#!/usr/bin/python3
from recipe import Recipe
from book import Book
b = Book("My seductive recipes")


recipe1 = Recipe("tortilla", 3, 45,
                 ["patatas", "huevos", "aceite", "sal"],
                 "pelar, batir, mezclar freir", "lunch")
recipe2 = Recipe("sandwich", 2, 30,
                 ["ham", "bread", "cheese", "tomatoes"],
                 "cortar untar colocar", "starter")
recipe3 = Recipe("cake", 4, 60,
                 ["flour", "sugar", "eggs"],
                 "mezclar todo", "starter")
recipe4 = Recipe("salad", 2, 15,
                 ["avocado", "arugula", "tomatoes", "spinach"],
                 "Alinyar", "lunch")
b.add_recipe(recipe1)
b.add_recipe(recipe2)
b.add_recipe(recipe3)
b.add_recipe(recipe4)


b.print_all()
print(b.creation_date)
print(b.last_update)

crumble = Recipe("Crumble", 1, 25,
                 ["apples", "flour", "sugar"],
                 "delicious", "dessert")
b.add_recipe(crumble)
print(b.last_update)

b.print_all()

b.add_recipe(crumble)
print(b.last_update)

b.print_all()
print("b.get_recipe_by_name('Crumble')")
b.get_recipe_by_name()

print("b.get_recipe_by_name('Liver Icecream')")
b.get_recipe_by_name("Liver Icecream")

print(b.get_recipes_by_types("dessert")[0])

b.get_recipes_by_types("asdasd")

for r in b.get_recipes_by_types("lunch"):
    print(r)
b.get_recipe_by_name()
