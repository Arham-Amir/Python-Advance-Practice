from _library import Library
import os
class AdminFactory:
    def __init__(self, library: Library):
        self.library = library
        print(self.library)
    
    def process_admin_functionalities(self):
        while True:
            os.system('cls||clear')
            self._display_menu()
            choice = self._get_input_choice()
            terminate = self._processInput(choice)
            if terminate:
                return
           
    def _display_menu(self):
        print("========\tAdmin Menu:\t========\n")
        print("1. View all books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Update book details")
        print("5. Details of all rented books")
        print("6. Exit")
    
    def _get_input_choice(self):
        try:
            choice = int(input("Enter your choice : "))
            if not (choice >= 1 and choice <= 6):
                choice = int(input("\nInvalid input!\nEnter your choice : "))
            return choice
        except:
            print("Choice should be integer value !\n")
            return self.get_input_choice()

    def _processInput(self, choice):
        os.system('cls||clear')
        if choice == 1:
            self.library.display_books()
            self._wait_for_key_to_continue()
            
        elif choice == 2:
            self.library.add_book()
            self._wait_for_key_to_continue()

        elif choice == 3:
            self.library.remove_book()
            self._wait_for_key_to_continue()
            
        elif choice == 4:
            self.library.update_book()
            self._wait_for_key_to_continue()
            
        elif choice == 5:
            self.library.display_all_users_rented_books() 
            self._wait_for_key_to_continue()
            
        else:
            return True 
       
    def _wait_for_key_to_continue(self):
        input("Enter any key to continue : ")
        os.system('cls||clear')
