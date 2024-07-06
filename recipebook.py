
recipes = []

while True:
    print("THE RECIPE BOOK")
    print("\n1.Add recipe \n2.View recipe \n3.Update recipe \n4.Delete recipe \n5.exit\n ")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        recipe_id = input("Enter Recipe ID: ")
        if any(recipe['recipe_id'] == recipe_id for recipe in recipes):
            print("Recipe ID already exists. Please enter a unique ID.\n")
        else:
            name = input("Enter Recipe Name: ")
            ingredients = input("Enter Ingredients (comma separated): ").split(',')
            instructions = input("Enter Instructions: ")
            recipes.append({"recipe_id": recipe_id, "name": name, "ingredients": ingredients, "instructions": instructions})
            print("Recipe added successfully!\n")
    
    elif choice == 2:
        if not recipes:
            print("\nNo recipes available.\n")
        else:
            print("\n{:<10} {:<20} {:<50}".format("ID", "Name", "Ingredients"))
            print("-" * 80)
            for recipe in recipes:
                print("{:<10} {:<20} {:<50}".format(recipe['recipe_id'], recipe['name'], ', '.join(recipe['ingredients'])))
                print("Instructions: " + recipe['instructions'])
                print("-" * 80)
            print("")
    
    elif choice == 3:
        recipe_id = input("Enter Recipe ID to update: ")
        found = False
        for recipe in recipes:
            if recipe['recipe_id'] == recipe_id:
                print("Current Name: " + recipe['name'])
                new_name = input("Enter new name (leave blank to keep current): ")
                recipe['name'] = new_name or recipe['name']
                
                print("Current Ingredients: " + ', '.join(recipe['ingredients']))
                new_ingredients = input("Enter new ingredients (comma separated, leave blank to keep current): ")
                recipe['ingredients'] = new_ingredients.split(',') if new_ingredients else recipe['ingredients']
                
                print("Current Instructions: " + recipe['instructions'])
                new_instructions = input("Enter new instructions (leave blank to keep current): ")
                recipe['instructions'] = new_instructions or recipe['instructions']
                
                print("Recipe updated successfully!\n")
                found = True
                break
        if not found:
            print("Recipe not found!\n")
    
    elif choice == 4:
        recipe_id = input("Enter Recipe ID to delete: ")
        for recipe in recipes:
            if recipe['recipe_id'] == recipe_id:
                recipes.remove(recipe)
                print("Recipe deleted successfully!\n")
                break
        else:
            print("Recipe not found!\n")
    
    elif choice == 5:
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.\n")

            