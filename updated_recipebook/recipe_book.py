from recipe import Recipe

class RecipeBook:
    def __init__(self):
        self.recipes = []
        self.add_default_recipes()

    def add_default_recipes(self):
        default_recipes = [
            {
                "recipe_id": "1",
                "name": "Spaghetti Carbonara",
                "ingredients": ["Spaghetti", "Eggs", "Parmesan cheese", "Pancetta", "Black pepper", "Salt"],
                "instructions": "1. Cook the spaghetti according to package instructions.\n"
                                "2. In a bowl, beat the eggs and mix in the grated Parmesan cheese.\n"
                                "3. In a pan, cook the pancetta until crispy.\n"
                                "4. Drain the spaghetti and add it to the pan with pancetta.\n"
                                "5. Remove from heat and quickly stir in the egg and cheese mixture.\n"
                                "6. Season with black pepper and salt to taste.\n"
                                "7. Serve immediately."
            },
            {
                "recipe_id": "2",
                "name": "Chicken Caesar Salad",
                "ingredients": ["Romaine lettuce", "Grilled chicken breast", "Croutons", "Parmesan cheese", "Caesar dressing", "Lemon juice", "Black pepper", "Salt"],
                "instructions": "1. Chop the romaine lettuce and place it in a large bowl.\n"
                                "2. Slice the grilled chicken breast and add it to the bowl.\n"
                                "3. Add croutons and grated Parmesan cheese.\n"
                                "4. Drizzle with Caesar dressing and lemon juice.\n"
                                "5. Toss to combine.\n"
                                "6. Season with black pepper and salt to taste.\n"
                                "7. Serve immediately."
            },
            {
                "recipe_id": "3",
                "name": "Chocolate Chip Cookies",
                "ingredients": ["All-purpose flour", "Baking soda", "Salt", "Unsalted butter", "Granulated sugar", "Brown sugar", "Eggs", "Vanilla extract", "Chocolate chips"],
                "instructions": "1. Preheat the oven to 350°F (175°C).\n"
                                "2. In a bowl, whisk together flour, baking soda, and salt.\n"
                                "3. In a separate bowl, cream together the butter, granulated sugar, and brown sugar.\n"
                                "4. Beat in the eggs and vanilla extract.\n"
                                "5. Gradually add the flour mixture to the wet ingredients and mix until combined.\n"
                                "6. Stir in the chocolate chips.\n"
                                "7. Drop spoonfuls of dough onto a baking sheet.\n"
                                "8. Bake for 10-12 minutes, or until golden brown.\n"
                                "9. Let cool on a wire rack before serving."
            },
            {
                "recipe_id": "4",
                "name": "Classic Margherita Pizza",
                "ingredients": ["Pizza dough", "Tomato sauce", "Fresh mozzarella cheese", "Fresh basil leaves", "Olive oil", "Salt"],
                "instructions": "1. Preheat the oven to the highest temperature.\n"
                                "2. Roll out the pizza dough and place it on a baking sheet.\n"
                                "3. Spread tomato sauce over the dough.\n"
                                "4. Arrange slices of fresh mozzarella cheese on top.\n"
                                "5. Bake in the oven until the crust is golden and the cheese is bubbly.\n"
                                "6. Remove from the oven and top with fresh basil leaves.\n"
                                "7. Drizzle with olive oil and sprinkle with salt.\n"
                                "8. Slice and serve."
            }
        ]

        for recipe in default_recipes:
            self.recipes.append(Recipe(recipe["recipe_id"], recipe["name"], recipe["ingredients"], recipe["instructions"]))

    def add_recipe(self):
        while True:
            recipe_id = input("Enter Recipe ID: ")
            if self.find_recipe(recipe_id):
                print("Recipe ID already exists. Please enter a unique ID.\n")
            else:
                name = input("Enter Recipe Name: ")
                ingredients = input("Enter Ingredients (comma separated): ").split(',')
                instructions = input("Enter Instructions: ")
                recipe = Recipe(recipe_id, name, ingredients, instructions)
                self.recipes.append(recipe)
                print("Recipe added successfully!\n")
                break

    def view_recipes(self):
        if not self.recipes:
            print("\nNo recipes available.\n")
        else:
            print("\n{:<10} {:<20} {:<50}".format("ID", "Name", "Ingredients"))
            print("-" * 80)
            for recipe in self.recipes:
                print("{:<10} {:<20} {:<50}".format(recipe.recipe_id, recipe.name, ', '.join(recipe.ingredients)))
                print("Instructions: " + recipe.instructions)
                print("-" * 80)
            print("")

    def update_recipe(self):
        recipe_id = input("Enter Recipe ID to update: ")
        recipe = self.find_recipe(recipe_id)
        if recipe:
            print("Current Name: " + recipe.name)
            new_name = input("Enter new name (leave blank to keep current): ")
            recipe.name = new_name or recipe.name
            
            print("Current Ingredients: " + ', '.join(recipe.ingredients))
            new_ingredients = input("Enter new ingredients (comma separated, leave blank to keep current): ")
            recipe.ingredients = new_ingredients.split(',') if new_ingredients else recipe.ingredients
            
            print("Current Instructions: " + recipe.instructions)
            new_instructions = input("Enter new instructions (leave blank to keep current): ")
            recipe.instructions = new_instructions or recipe.instructions
            
            print("Recipe updated successfully!\n")
        else:
            print("Recipe not found!\n")

    def delete_recipe(self):
        recipe_id = input("Enter Recipe ID to delete: ")
        recipe = self.find_recipe(recipe_id)
        if recipe:
            self.recipes.remove(recipe)
            print("Recipe deleted successfully!\n")
        else:
            print("Recipe not found!\n")

    def find_recipe(self, recipe_id):
        for recipe in self.recipes:
            if recipe.recipe_id == recipe_id:
                return recipe
        return None
