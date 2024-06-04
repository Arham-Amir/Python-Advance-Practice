from _library import Library
from _user import User
from utilities import *
import os
class UserFactory:
    def __init__(self, library:Library):
        self.library = library
    
    def get_userid_input(self):
        id_number = get_string_input("Enter your Identity Number: ")
        return User(id_number)
        
    def process_user_functionalities(self):
        os.system('cls||clear')
        user = self.get_userid_input()
        while True:
            os.system('cls||clear')
            print(f"Welcome User-{user.user_identity_number} :d\n")
            self._display_menu()
            choice = self._get_input_choice()
            terminate = self._processInput(choice, user)
            if terminate:
                return
        
    def _display_menu(self):
        print("========\tMenu:\t========\n")
        print("1. View all books")
        print("2. Rent a book")
        print("3. Return a book")
        print("4. Details of rented books")
        print("5. Exit")
        
    def _get_input_choice(self):
        try:
            choice = int(input("Enter your choice : "))
            if not (choice >= 1 and choice <= 5):
                choice = int(input("\nInvalid input!\nEnter your choice : "))
            return choice
        except:
            print("Choice should be integer value !\n")
            return self.get_input_choice()

    def _processInput(self, choice, user):
        os.system('cls||clear')
        if choice == 1:
            self.library.display_books()
            self._wait_for_key_to_continue()
            
        elif choice == 2:
            self.library.rent_book(user)
            self._wait_for_key_to_continue()

        elif choice == 3:
            self.library.return_book(user)
            self._wait_for_key_to_continue()
            
        elif choice == 4:
            user_has_any_book = self.library.display_user_rented_books(user)
            if (not user_has_any_book):
                print("You haven't borrowed any book.\n")
            self._wait_for_key_to_continue()
            
        else:
            return True 
             
    def _wait_for_key_to_continue(self):
        input("Enter any key to continue : ")
        os.system('cls||clear')
