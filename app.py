from flask import Flask, request, jsonify
from models import Product
from services import analyze_product

app = Flask(__name__)

@app.route("/product/analyze", methods=["POST"])
def analyze():
    data = request.json

    product = Product(
        data.get("name"),
        data.get("cost"),
        data.get("price"),
        data.get("competition"),
        data.get("demand"),
        data.get("shipping_days")
    )

    result = analyze_product(product)
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)
