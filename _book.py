import time
from utilities import *

class Book:
    def __init__(self, _title, _author, _available=True, _id = str(int(time.time() * 1000))) -> None:
        self.id = _id
        self.title = _title
        self.author = _author
        self.available = _available

    @staticmethod
    def new_book():
        book_title = get_string_input("Enter the title of the book: ")
        author = get_string_input("Enter the author of the book: ")
        return Book(book_title, author)
        
    def __repr__(self):
        return f"Book id : {self.id}, Title : {self.title}, Author : {self.author}, Available : {self.available}"
    
    def toString(self):
        return f"{self.id},{self.title},{self.author},{self.available}"
