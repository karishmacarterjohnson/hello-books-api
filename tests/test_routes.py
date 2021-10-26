from flask import jsonify
def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

def test_get_one_book_with_no_data(client):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 404

def test_get_all_books_with_records(client, two_saved_books):
    response = client.get("/books")
    response_body = response.get_json()
    book_1 = {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }
    book_2 = {
        "id": 2,
        "title": "Mountain Book",
        "description": "i luv 2 climb rocks"
    }
    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert book_1 in response_body
    assert book_2 in response_body

def test_post_data_gives_201(client):
    
    response = client.post("/books", 
        json = {"title": "River Book", "description": "it gets water"})
    
    assert response.status_code == 201 