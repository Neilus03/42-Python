cookbook = {
    		'bocadillo': 
            	{
    			 'ingredients': ["jamón", "pan", "queso", "tomate"],
             	 'meal': 'almuerzo',
             	 'prep_time' : 10
            	},
            'tarta': 
            	{
      			 'ingredients': ["harina", "azúcar", "huevos"],
                 'meal': 'postre',
                 'prep_time' : 60
                 },
			
			'ensalada': 
            	{
				 'ingredients': ["aguacate", "rúcula", "tomates", "espinacas"],
                 'meal': 'almuerzo',
                 'prep_time' : 15
				}
			}

def print_recipe_names(cookbook):
	recetas = "Las recetas de este cookbook son: "
	for k in cookbook.keys():
		recetas += str(k) + ", "
	recetas = recetas.strip(", ")
	return (recetas)

def details(recipe, cookbook):
	detalles = "Los detalles para hacer " + str(recipe) + " son: "
	detalles += str(cookbook[recipe])
	return (detalles)

def delete(recipe, cookbook):
	if recipe in cookbook:
		del cookbook[recipe]
	return "updated cookbook", cookbook

def add_recipe(cookbook):
    name = input("Ingrese el nombre de la receta: ")
    ingredients = input("Ingrese los ingredientes de la receta (separados por espacios): ").split(" ")
    meal = input("Ingrese el tipo de comida de la receta: ")
    prep_time = int(input("Ingrese el tiempo de preparación en minutos de la receta: "))
    cookbook[name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}
    return cookbook

print(
	"Welcome to the Python Cookbook !\n"
	"List of available option:\n"
	"1: Add a recipe\n"
	"2: Delete a recipe\n"
	"3: Print a recipe\n"
	"4: Print the cookbook\n"
	"5: Quit\n",
	)
option = int(input("Please select an option: "))

while (option):
	if option not in [1, 2, 3, 4, 5]:
		print("Sorry, this option does not exist")
	elif option == 1:
		print(add_recipe(cookbook))
	elif option == 2:
		recipe = str(input("Recipe to delete: "))
		if recipe not in cookbook:
			print("This recipe is not in the cookbook")
		else:
			print(delete(recipe, cookbook))
	elif option == 3:
		recipe = str(input("Recipe to see in detail: "))
		if recipe not in cookbook:
			print("This recipe is not in the cookbook")
		else:
			print(details(recipe, cookbook))
	elif option == 4:
		print(print_recipe_names(cookbook))
	if option != 5:
		option = int(input("Please select an option: "))
	else:
		print("Cookbook closed. Goodbye !")
		break