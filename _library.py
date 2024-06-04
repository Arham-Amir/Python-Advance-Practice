from _book import Book
from _user import User
from utilities import *
import threading

class Library:
    def __init__(self) -> None:
        self.filepath = './library.txt'
        self.user_rented_record = './userRecords.txt'
        self.books = []
        self.lock = threading.Lock()
        self._load_books()
        
    def _load_books(self):
        with self.lock:
            try:
                with open(self.filepath, 'r+') as file:
                    for line in file:
                        id, book_title, author, available = line.strip().split(',')
                        self.books.append(
                            Book(book_title, author, available == 'True', id))
            except:
                print("Error in opening file library.txt")
                pass

    def add_book(self):
        new_book = Book.new_book()
        for book in self.books:
            if book.title == new_book.title:
                print(f"Book with the title '{new_book.title}' already exist !")
                return
        with self.lock:
            with open(self.filepath, 'a') as file:
                file.write(f"{new_book.id},{new_book.title},{new_book.author},{new_book.available}\n")
            self.books.append(new_book)
        print("Book Added Sucessfully !")

    def display_books(self):
        if self.books != []:
            for book in self.books:
                print(book)
            print()
        else:
            print("We dont have any Book in library right now.\n") 
        
    def display_available_books(self):
        if self.books != []:
            for book in self.books:
                book.available and print(book)
            print()
            return True
        else:
            return False 
    
    def display_user_rented_books(self, user:User):
        if user.rented_books_list != []:
            for book in user.rented_books_list:
                for av_book in self.books:
                    if book == av_book.id:
                        print(av_book)
                        break
            print()
            return True
        else:
            return False 
           
    def display_all_users_rented_books(self):
        if User.users_record != {}:
            for userid, books in User.users_record.items():
                print(f"User-{userid}:")
                for book in books:
                    for av_book in self.books:
                        if book == av_book.id:
                            print("\t", av_book)
                            break    
            print()
        else:
            print("No Rented book. All books are available in library.\n")
    
    def remove_book(self):
        self.display_books()
        input_book_id = get_string_input("Enter the Book ID: ")
        with self.lock:
            for book in self.books:
                if book.id == input_book_id:
                    self.books.remove(book)
                    self._update_file()
                    print(f"Book with id '{input_book_id}' removed successfully.")
                    return
            print(f"Book with id '{input_book_id}' not found.")

    def update_book(self):
        self.display_books()
        input_book_id = get_string_input("Enter Book ID: ")
        input_book_title = get_string_input("Enter the updated title of the book: ")
        input_book_author = get_string_input("Enter the updated author of the book: ")
        with self.lock:
            for book in self.books:
                if book.id == input_book_id:
                    if(book.available):
                        book.title = input_book_title
                        book.author = input_book_author
                        self._update_file()
                        print(f"Book with id '{input_book_id}' updated successfully.")
                        return
                    else:
                        print(f"Book with id '{input_book_id}' not available in library so you cant update it right now.")
                        return
            print(f"Book with id '{input_book_id}' not found.")

    def _update_file(self):
        with open(self.filepath, 'w') as file:
            for book in self.books:
                file.write(f"{book.id},{book.title},{book.author},{book.available}\n")

    def rent_book(self, user:User):
        any_book = self.display_available_books()
        if(any_book):
            input_book_id = get_string_input("Enter Book ID: ")
            with self.lock:
                for book in self.books:
                    if book.id == input_book_id and book.available:
                        book.available = not book.available
                        self._update_file()
                        user.rent_book(book)
                        print(f"Book with id '{input_book_id}' rented successfully.")
                        return
                print(f"Book with id '{input_book_id}' not available.")
        else:
            print("Sorry. No Book available in library at this time.\n")
            
    def return_book(self, user:User):
        user_has_any_book = self.display_user_rented_books(user)
        if(user_has_any_book):
            input_book_id = get_string_input("Enter Book ID: ")
            with self.lock:
                for book in self.books:
                    if book.id == input_book_id and not book.available:
                        book.available = not book.available
                        self._update_file()
                        user.return_book(book)
                        print(f"Book with id '{input_book_id}' returned successfully.")
                        return
                print(f"Book with id '{input_book_id}' not available.")
        else:
            print("You haven't borrowed any book.\n")