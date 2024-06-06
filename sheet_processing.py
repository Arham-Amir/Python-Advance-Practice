import os
import pandas as pd
from utilities import *

df = pd.read_csv("./pokemon_data.csv")
    
def display_menu_options():
    print("1. Display All Pokemons Records")
    print("2. Search Pokemon by name")
    print("3. Search Pokemon by type")
    print("4. Top 5 Pokemons with greater HP")
    print("5. Top 5 Legendary pokemons")
    print("6. Top 5 Pokemons with greater attack")
    print("7. Top 5 Pokemons with greater defense")
    print("8. Exit")

def get_input_choice():
    try:
        num = int(input("Enter Choice: "))
        while not (num >= 1 and num <= 8):
            num = int(input("\nInvalid number. Enter Choice: "))
        return num
    except Exception as e:
        print(e, "\n")
        return get_input_choice()

def input_to_continue():
    input("Enter any key to continue. ")
    
def process_input_choice(choice):
    os.system("cls")
    if choice == 1:
        display_all_pokemons()
    if choice == 2:
        search_pokemon_by_name()
    if choice == 1:
        search_pokemon_by_type()
    if choice == 4:
        pokemon_with_greater_hp()
    if choice == 5:
        legendary_pokemons()
    if choice == 6:
        pokemon_with_greater_attack()
    if choice == 7:
        pokemon_with_greater_defense()
    if choice == 8:
        return
    input_to_continue()
    
def display_all_pokemons():
    rows_per_page = 10
    total_rows = len(df)
    num_pages = -(-total_rows // rows_per_page)
    
    page = 0
    while True:
        os.system('cls')
        start_index = page * rows_per_page
        end_index = min((page + 1) * rows_per_page, total_rows)
        print(df.iloc[start_index:end_index])
        print("\nPage {}/{}".format(page + 1, num_pages))
        print("Press any key to show the next page, or 'q' to quit.")
        
        key = input()
        
        if key.lower() == 'q':
            break
        else:
            page = (page + 1) % num_pages
    
def search_pokemon_by_name():
    pokemon_name = input("Enter Pokemon Name: ")
    pokemon_details = df.loc[df['Name'] == pokemon_name]
    
    if not pokemon_details.empty:
        print(pokemon_details)
    else:
        print(f"No Pokémon with the name '{pokemon_name}' found.")
        
def search_pokemon_by_type():
    pokemon_type = input("Enter Pokemon Type 1: ")
    pokemon_details = df.loc[df['Type 1'] == pokemon_type]
    
    if not pokemon_details.empty:
        print(pokemon_details)
    else:
        print(f"No Pokémon with the name '{pokemon_type}' found.")
  
def pokemon_with_greater_hp():
    top_5 = df.sort_values(['HP'], ascending=False).head()
    print(top_5[["Name", "HP"]].reset_index(drop=True))
  
def legendary_pokemons():
    legendary_pokemons = True
    pokemon_details = df.loc[df['Legendary'] == legendary_pokemons].head()
    
    if not pokemon_details.empty:
        print(pokemon_details)
    else:
        print(f"No legendary pokemon found.")

def pokemon_with_greater_attack():
    top_5 = df.sort_values(['Attack'], ascending=False).head()
    print(top_5[["Name", "Attack"]].reset_index(drop=True))
    
def pokemon_with_greater_defense():
    top_5 = df.sort_values(['Defense'], ascending=False).head()
    print(top_5[["Name", "Defense"]].reset_index(drop=True))
    
if __name__ == "__main__":
    display_menu_options()
    choice = get_input_choice()
    process_input_choice(choice)