import product_management

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Product")
        print("2. List Products")
        print("3. Update Product Stock")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            print(product_management.add_product(product_id, name, price, stock))
        elif choice == "2":
            products = product_management.list_products()
            for product_id, details in products.items():
                print(f"{product_id}: {details['name']} - ${details['price']} (Stock: {details['stock']})")
        elif choice == "3":
            product_id = input("Enter product ID: ")
            stock = int(input("Enter new stock: "))
            print(product_management.update_stock(product_id, stock))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
