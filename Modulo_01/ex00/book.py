from datetime import *

class Book:
    def __init__(self, name: str, last_update: datetime, creation_date: datetime, recipes_list: dict):
        self.name = name
        self.last_update = datetime.strptime(last_update, '%b %d %Y')
        self.creation_date = datetime.strptime(creation_date, '%b %d %Y')
        self.recipes_list = recipes_list
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "\n"
        txt += f"{self.name}: {self.name}\n"
        txt += f"\nÚltima actualización: {self.last_update.strftime('%Y-%m-%d')}\n"
        txt += f"\nFecha de creación: {self.creation_date.strftime('%Y-%m-%d')}\n"
        txt += "\nLista de recetas:\n"
        for type, recipes in self.recipes_list.items():
            txt += f"- {type}: {recipes}\n"
        return txt

    def get_recipe_by_name(self, name):
        """Return the recipe instance with the given name"""
        for recipe_names in self.recipes_list.values():
            for recipe_name in recipe_names:
                if recipe_name == name:
                    print(f"Receta enccontrada: {recipe_name}")
                    return recipe_name
    print(f"No se encontró una receta con ese nombre")


    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type"""
        recipes = self.recipes_list.get(recipe_type.lower())
        if recipes:
            print(f"{recipe_type} recipes:",[recipe for recipe in recipes])
        else:
            print(f"No se encontraron recetas de tipo {recipe_type}")

    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        self.recipes_list.setdefault(recipe.recipe_type.lower(), []).append(recipe.name)
        self.last_update = datetime.now()
        print(f"Receta {recipe.name} añadida al libro")

