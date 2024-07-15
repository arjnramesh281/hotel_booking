products = {
    "p1": {"name": "Dog Collar", "price": 15.99, "stock": 10},
    "p2": {"name": "Cat Toy", "price": 7.99, "stock": 20},
    "p3": {"name": "Bird Cage", "price": 45.00, "stock": 5},
    "p4": {"name": "Fish Tank", "price": 60.00, "stock": 3},
    "p5": {"name": "Hamster Wheel", "price": 12.99, "stock": 8}
}

def add_product(product_id, name, price, stock):
    if product_id in products:
        raise Exception("Product already exists.")
    products[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }
    return "Product added successfully."

def list_products():
    return products

def update_stock(product_id, stock):
    if product_id not in products:
        raise Exception("Product not found.")
    products[product_id]["stock"] = stock
    return "Stock updated successfully."
