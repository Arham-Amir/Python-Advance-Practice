import threading
import json
from _book import Book

class User:
    users_record = {}
    lock = threading.Lock()
    filepath = 'users_record.txt'
    
    def __init__(self, _id_number) -> None:
        self.user_identity_number = _id_number
        self.rented_books_list = self.load_particular_user_record(_id_number)

    @staticmethod
    def load_users_record():
        with User.lock:
            try:
                with open(User.filepath, 'r+') as file:
                    for line in file:
                        user_id, book_id = line.strip().split(',')
                        if user_id in User.users_record:
                            User.users_record[user_id].append(book_id)
                        else:
                            User.users_record[user_id] = [book_id]
            except:
                pass
 
    def load_particular_user_record(self, user_id):
        if user_id in User.users_record:
            return User.users_record[user_id]
        else:
            return []
        
    def rent_book(self, _book):
        self.rented_books_list.append(_book.id)
        if self.user_identity_number in User.users_record:
            User.users_record[self.user_identity_number].append(_book.id)
        else:
            User.users_record[self.user_identity_number] = [_book.id]
        with User.lock:
            with open(User.filepath, 'a') as file:
                file.write(f"{self.user_identity_number},{_book.id}\n")
        print("Book Borrowed Sucessfully !")        

    def return_book(self, _book):
        if _book.id in self.rented_books_list:
            self.rented_books_list.remove(_book.id)
            print(User.users_record)
            User.users_record[self.user_identity_number].remove(_book.id)
            self._update_file()
            print("Book Returned Sucessfully.")
        else:
            print(f"User {self.user_identity_number} dont have book with id {_book.id}.")

    def _update_file(self):
        with User.lock:
            with open(User.filepath, 'w') as file:
                for id, books in User.users_record.items():
                    for book_id in books: 
                        file.write(f"{id},{book_id}\n")
            