from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated cart with product IDs
CART = ["101", "102"]

@app.route("/", methods=["GET"])
def landing_page():
    return jsonify({
        "message": "Welcome to the Cart Service!",
        "endpoints": {
            "GET /cart": "View items in the cart",
            "POST /cart": "Add a product ID to the cart",
            "DELETE /cart/<product_id>": "Remove a specific product from the cart",
            "DELETE /cart": "Clear the cart"
        }
    })

@app.route("/cart", methods=["GET"])
def get_cart():
    return jsonify({"product_ids": CART})

@app.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    product_id = data.get("product_id")
    
    if not product_id:
        return jsonify({"error": "product_id is required"}), 400
    
    CART.append(product_id)
    return jsonify({"message": f"Product {product_id} added to cart", "cart": CART}), 201

@app.route("/cart/<product_id>", methods=["DELETE"])
def remove_from_cart(product_id):
    if product_id in CART:
        CART.remove(product_id)
        return jsonify({"message": f"Product {product_id} removed from cart", "cart": CART})
    else:
        return jsonify({"error": "Product not in cart"}), 404

@app.route("/cart", methods=["DELETE"])
def clear_cart():
    CART.clear()
    return jsonify({"message": "Cart cleared", "cart": CART})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
