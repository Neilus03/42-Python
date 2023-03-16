class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: str, recipe_type: str):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "\n"
        txt += f"{self.name}: {self.recipe_type}\n"
        txt += f"\nDificultad: {'+' * self.cooking_lvl}\n"
        txt += f"\nTiempo de preparación: {self.cooking_time} min\n"
        txt += "\nIngredientes:\n"
        for ingredient in self.ingredients:
            txt += f"- {ingredient}\n"
        txt += f"\nDescripción: {self.description}\n"
        return txt

    