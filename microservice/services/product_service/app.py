from flask import Flask, jsonify, request

app = Flask(__name__)

PRODUCTS = {
    "101": {"id": "101", "name": "Laptop", "price": 1000},
    "102": {"id": "102", "name": "Phone", "price": 500},
    "103": {"id": "103", "name": "Headphones", "price": 150}
}

@app.route("/", methods=["GET"])
def landing_page():
    return jsonify({
        "message": "Welcome to the Product Service!",
        "endpoints": {
            "/products": "List all products",
            "/products/<product_id>": "Get a specific product by ID"
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
