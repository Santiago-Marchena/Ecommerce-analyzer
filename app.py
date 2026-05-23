from flask import Flask, request, jsonify, render_template
from models import Product
from services import analyze_product
import os
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)