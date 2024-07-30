from recipe_book import RecipeBook
from user_management import UserManagement

def main():
    user_management = UserManagement()
    recipe_book = RecipeBook()
    
    while True:
        print("Welcome to the Recipe Book")
        print("\n1. Register \n2. Login \n3. View Recipes \n4. Exit\n")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            user_management.register()
        elif choice == 2:
            if user_management.login():
                while True:
                    print("THE RECIPE BOOK")
                    print("\n1. Add recipe \n2. View recipes \n3. Update recipe \n4. Delete recipe \n5. Logout\n")
                    user_choice = int(input("Enter your choice: "))
                    
                    if user_choice == 1:
                        recipe_book.add_recipe()
                    elif user_choice == 2:
                        recipe_book.view_recipes()
                    elif user_choice == 3:
                        recipe_book.update_recipe()
                    elif user_choice == 4:
                        recipe_book.delete_recipe()
                    elif user_choice == 5:
                        print("Logged out..!")
                        break
                    else:
                        print("Invalid choice! Please try again.\n")
        elif choice == 3:
            recipe_book.view_recipes()
        elif choice == 4:
            print("Exited..!")
            break
        else:
            print("Invalid choice! Please try again.\n")

main()
