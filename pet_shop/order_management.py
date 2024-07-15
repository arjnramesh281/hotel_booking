from product_management import products

orders = []
order_id_counter = 1

def place_order(username, product_id, quantity):
    global order_id_counter
    if product_id not in products:
        raise Exception("Product not found.")
    if products[product_id]["stock"] < quantity:
        raise Exception("Insufficient stock.")
    products[product_id]["stock"] -= quantity  # Reduce the stock
    order_id = order_id_counter
    order_id_counter += 1
    order = {
        "order_id": order_id,
        "username": username,
        "product_id": product_id,
        "quantity": quantity
    }
    orders.append(order)
    return f"Order placed successfully. Your order ID is {order_id}."

def cancel_order(username, order_id):
    global orders
    for order in orders:
        if order["username"] == username and order["order_id"] == order_id:
            # Increase the stock of the canceled product
            product_id = order["product_id"]
            products[product_id]["stock"] += order["quantity"]
            # Remove the order from the list
            orders.remove(order)
            return f"Order {order_id} canceled successfully."
    raise Exception("Order not found.")

def list_orders():
    return orders
