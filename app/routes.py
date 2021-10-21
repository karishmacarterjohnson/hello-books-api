from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

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

'''
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
'''