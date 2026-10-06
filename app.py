from flask import Flask, jsonify

app = Flask(__name__)

BOOKS = [
    {"id": 1, "title": "Cien anos de soledad", "author": "Gabriel Garcia Marquez"},
    {"id": 2, "title": "El coronel no tiene quien le escriba", "author": "Gabriel Garcia Marquez"},
    {"id": 3, "title": "Rayuela", "author": "Julio Cortazar"},
]


@app.get("/")
def index():
    return "python-example OK"


@app.get("/books")
def books():
    return jsonify(BOOKS)
