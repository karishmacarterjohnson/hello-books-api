from flask import Blueprint, jsonify

hello_world_bp = Blueprint("hello_world", __name__)
   
@hello_world_bp.route("/hello-world", methods = ["GET"])
def hello_endpoint():
    body = "Hello, World!"
    return body

@hello_world_bp.route("/hello/JSON", methods = ["GET"])
def karishma_info():
    karishma_body = {
        "name": "Karishma Johnson",
        "message": "What's up?",
        "hobbies": ["swimming", "rowing", "throwing", "printmaking"]
    }

    return karishma_body

'''
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "No Longer Human", "Osamu Dazai's descent"),
    Book(2, "Tian Guan Ci Fu", "Ghost King and Fallen God fall in love"),
    Book(3, "Grokking Algorithms", "Visual coding lesson")
]
'''

books_bp = Blueprint("books", __name__, url_prefix="/books")
## /books is the group route, 
## "books" is the debug name
## use blueprint for all RESTful routes beginning w /books

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response) # 200 OK

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }