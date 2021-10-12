from flask import Blueprint

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