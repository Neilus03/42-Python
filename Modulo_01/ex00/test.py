
from book import Book
from recipe import Recipe
from datetime import *

newbook = Book("Mi newbook", "Feb 8 2022", "Jun 1 2021", {"starter": ['recipe1', 'recipe2'], "lunch": ['recipe3', 'recipe4'], "dessert": ['recipe5'] })
tourte = Recipe("Tourte", 3, 60, ["harina", "azúcar", "mantequilla", "manzanas"], "Una deliciosa tarta de manzana", "postre")

newbook.add_recipe(tourte)
newbook.get_recipe_by_name('recipe1')
newbook.get_recipes_by_types('starter')

print(newbook)
