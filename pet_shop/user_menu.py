import product_management
import order_management

def user_menu(username):
    while True:
        print("\nUser Menu:")
        print("1. List Products")
        print("2. Place Order")
        print("3. View Order History")
        print("4. Cancel Order")
        print("5. Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            products = product_management.list_products()
            for product_id, details in products.items():
                print(f"{product_id}: {details['name']} - ${details['price']} (Stock: {details['stock']})")
        elif choice == "2":
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity: "))
            try:
                print(order_management.place_order(username, product_id, quantity))
            except Exception as e:
                print(e)
        elif choice == "3":
            orders = order_management.list_orders()
            for order in orders:
                if order["username"] == username:
                    print(order)
        elif choice == "4":
            order_id = int(input("Enter order ID to cancel: "))
            try:
                print(order_management.cancel_order(username, order_id))
            except Exception as e:
                print(e)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
