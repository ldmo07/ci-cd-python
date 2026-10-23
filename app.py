from flask import Flask, jsonify

app = Flask(__name__)

BOOKS = [
    {"id": 1, "title": "Cien anos de soledad", "author": "Gabo (G. Garcia Marquez)"},
    {"id": 2, "title": "El coronel no tiene quien le escriba", "author": "Gabo (G. Garcia Marquez)"},
    {"id": 3, "title": "Rayuela", "author": "J. Cortazar"},
]


PRODUCTS = [
    {"id": 1, "name": "Teclado mecanico", "price": 250000},
    {"id": 2, "name": "Mouse inalambrico", "price": 90000},
    {"id": 3, "name": "Monitor 24\"", "price": 680000},
]


CITIES = [
    {"id": 1, "name": "Bogota", "country": "Colombia"},
    {"id": 2, "name": "Medellin", "country": "Colombia"},
    {"id": 3, "name": "Cali", "country": "Colombia"},
]


@app.get("/")
def index():
    return "python-example OK"


@app.get("/books")
def books():
    return jsonify(BOOKS)


@app.get("/cities")
def cities():
    return jsonify(CITIES)


@app.get("/products")
def products():
    return jsonify(PRODUCTS)


@app.get("/products/<int:product_id>")
def product(product_id):
    found = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if found is None:
        return jsonify({"error": "product not found"}), 404
    return jsonify(found)
