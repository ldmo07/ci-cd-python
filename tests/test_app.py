from app import app


def test_index():
    res = app.test_client().get("/")
    assert res.status_code == 200
    assert b"python-example" in res.data


def test_books():
    res = app.test_client().get("/books")
    assert res.status_code == 200
    books = res.get_json()
    assert len(books) == 3
    assert all({"id", "title", "author"} <= b.keys() for b in books)


def test_products():
    res = app.test_client().get("/products")
    assert res.status_code == 200
    assert len(res.get_json()) == 3


def test_product_by_id():
    res = app.test_client().get("/products/2")
    assert res.status_code == 200
    assert res.get_json()["id"] == 2


def test_product_not_found():
    res = app.test_client().get("/products/99")
    assert res.status_code == 404