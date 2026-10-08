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