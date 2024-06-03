import random
import os

MAX_TRIES = 10
HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
   ========='''
   ,'''
    +---+
    |   |
    o   |
        |
        |
        |
   =========''',
   '''
    +---+
    |   |
    o   |
    |   |
        |
        |
   =========''',
   '''
    +---+
    |   |
    o   |
   /|   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\\  |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\\  |
   /    |
        |
   ========''','''
    +---+
    |   |
    o   |
   /|\\  |
   / \\  |
        |
   ========''']

words = "ape cat dog baboon elephant giraffe apple coconut monkey rubik mice mouse pineapple android apple house fence python grail zerg protoss terran llama fire policeman mamerto smad zebra lion luffy nigga universidad".split()

def printCurrentLevel(guessed_letters, tries):
    print("Tries Left: ", MAX_TRIES - tries)
    print("================================\n")
    print(HANGMANPICS[tries])
    print()
    print(guessed_letters)

def wantRestart():
    inp = input("Enter R to restart the match")
    if inp == 'R' or inp == 'r':
        return True
    return False

def setGameVar():
    word = random.choice(words)
    return word, "_" * len(word), 0

def result(word, guessed_letters):
    if guessed_letters == word:
        print("Hurray! You guessed the word.")
    else:
        print("Alas! You failed to guess the word.")
        
def getInputAndProcess(word, guessed_letters, tries):
    flag = False
    guessed_letters_list = list(guessed_letters)
    inp = input("Enter any letter : ").lower()
    if len(inp) == 1 and inp.isalpha():
        for i, el in enumerate(guessed_letters_list):
            if el == "_" and word[i] == inp:
                guessed_letters_list[i] = inp
                flag = True
                break
        if flag == True:
            print("Your guess is correct :)\n")
            return "".join(guessed_letters_list), tries
        else:
            print("You made a wrong guess :(\n")
            return guessed_letters, tries + 1
        
    else:
        return inp, MAX_TRIES
    
  
def game():
    global MAX_TRIES
    (word, guessed_letters, tries) = setGameVar()
    MAX_TRIES = len(word)
    
    while tries< MAX_TRIES and guessed_letters != word:
        os.system('cls||clear')
        print(word)
        printCurrentLevel(guessed_letters, tries)
        (guessed_letters, tries) = getInputAndProcess(word, guessed_letters, tries)
        
    print("\nThe Word is : ", word)
    result(word, guessed_letters)
    
    

game()
    
        