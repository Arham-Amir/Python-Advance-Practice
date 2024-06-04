from _library import Library
from _admin_factory import AdminFactory
from _user_factory import UserFactory
from _user import User
import os

def display_menu():
    print("========\tMenu:\t========\n")
    print("1. I am User")
    print("2. I am Admin")
    print("3. Exit")
    
def get_input_choice():
    try:
        choice = int(input("Enter your choice : "))
        if not (choice > 0 and choice < 4):
            choice = int(input("\nInvalid input!\nEnter your choice : "))
        return choice
    except:
        print("Choice should be integer value !\n")
        return get_input_choice()

def processInput(library: Library, choice):
    if choice == 1:
        user = UserFactory(library)
        user.process_user_functionalities()
        return False
    elif choice == 2:
        admin = AdminFactory(library)
        admin.process_admin_functionalities()   
        return False 
    else:
        return True
    
if __name__ == "__main__":
    library = Library()
    User.load_users_record()
    while True:
        display_menu()
        choice = get_input_choice()
        terminate = processInput(library, choice)
        if terminate:
            print("\nThanks for visiting our library. Allah Hafiz")
            break
        os.system('cls||clear')