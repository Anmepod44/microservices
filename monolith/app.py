from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated product database
PRODUCTS = {
    "101": {"id": "101", "name": "Laptop", "price": 1000},
    "102": {"id": "102", "name": "Phone", "price": 500},
    "103": {"id": "103", "name": "Headphones", "price": 150}
}

# Simulated cart storing product IDs
CART = ["101", "102"]

@app.route("/", methods=["GET"])
def landing_page():
    return jsonify({
        "message": "Welcome to the Product + Cart Service!",
        "endpoints": {
            "GET /products": "List all products",
            "GET /products/<product_id>": "Get details of a product",
            "GET /cart": "View cart with product details",
            "POST /cart": "Add product ID to cart",
            "DELETE /cart/<product_id>": "Remove product ID from cart",
            "DELETE /cart": "Clear all items from the cart"
        }
    })

@app.route("/products", methods=["GET"])
def list_products():
    return jsonify(list(PRODUCTS.values()))

@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    product = PRODUCTS.get(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route("/cart", methods=["GET"])
def get_cart():
    cart_items = [PRODUCTS[pid] for pid in CART if pid in PRODUCTS]
    return jsonify({"cart": cart_items})

@app.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    product_id = data.get("product_id")
    if not product_id:
        return jsonify({"error": "product_id is required"}), 400
    if product_id not in PRODUCTS:
        return jsonify({"error": "Product does not exist"}), 404

    CART.append(product_id)
    return jsonify({"message": f"Product {product_id} added to cart", "cart": CART}), 201

@app.route("/cart/<product_id>", methods=["DELETE"])
def remove_from_cart(product_id):
    if product_id in CART:
        CART.remove(product_id)
        return jsonify({"message": f"Product {product_id} removed from cart", "cart": CART})
    else:
        return jsonify({"error": "Product not in cart"}), 404
