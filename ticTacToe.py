import os

BOARD_SIZE = 4

SIGNS = {
    1: 'X',
    2: 'O'
}

def displayBoard(board):
    for i in range(0, BOARD_SIZE*BOARD_SIZE, BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i+j], end="  |  ")  
        print()
    print()

def checkColumn(board, currentTurn, last_marked_position):
    i = last_marked_position
    while i + BOARD_SIZE < BOARD_SIZE * BOARD_SIZE: # above current
        if not board[i + BOARD_SIZE] == SIGNS[currentTurn]:
            return False
        i += BOARD_SIZE
    i = last_marked_position
    while i - BOARD_SIZE >= 0: # below current
        if not board[i - BOARD_SIZE] == SIGNS[currentTurn]:
            return False
        i -= BOARD_SIZE
        
    return True

def checkRow(board, currentTurn, last_marked_position):
    i = last_marked_position
    while (i + 1) % BOARD_SIZE != 0: # above current
        if not board[i + 1] == SIGNS[currentTurn]:
            return False
        i += 1
    i = last_marked_position
    while i % BOARD_SIZE != 0: # below current
        if not board[i - 1] == SIGNS[currentTurn]:
            return False
        i -= 1
        
    return True

def checkDiagonal(board, currentTurn):
    count = 0
    for i in range(0, BOARD_SIZE * BOARD_SIZE, BOARD_SIZE + 1):
        if board[i] != SIGNS[currentTurn]:
            count = 0
            break
        else:
            count += 1
    if count == BOARD_SIZE:
        return True
    
    count = 0
    for i in range(BOARD_SIZE - 1, BOARD_SIZE * BOARD_SIZE, BOARD_SIZE - 1):
        if board[i] != SIGNS[currentTurn]:
            count = 0
            break
        else:
            count += 1
    if count == BOARD_SIZE:
        return True
    
    return False

def evaluate(board, currentTurn, last_marked_position):
    if checkColumn(board, currentTurn, last_marked_position): # for check in column
         return True
    elif checkRow(board, currentTurn, last_marked_position): # for check in row
        return True       
    elif checkDiagonal(board, currentTurn): # for check in diagonal
        return True
    else:
        return False

def getInputAndProcess(board, currentTurn):
    print(f"Player {currentTurn} Turn :-\n")
    input_position = int(input(f"Enter Position from 0-{BOARD_SIZE**2-1} : "))
    if not (0 <= input_position <= BOARD_SIZE**2-1) or board[input_position] != '_':
        input_position = int(input(f"\nInvalid Position.\nEnter Position from 0-{BOARD_SIZE**2-1} : "))
    
    board[input_position] = SIGNS[currentTurn]
    return input_position
  
def displayThings(dummy_board, board):
    os.system('cls||clear')
    displayBoard(dummy_board)
    displayBoard(board)
    
def game():  
    board = ['_'] * BOARD_SIZE*BOARD_SIZE
    dummy_board = [i for i in range(BOARD_SIZE*BOARD_SIZE)]
    currentTurn = 1
    displayThings(dummy_board, board)
    while '_' in board:
        last_marked_position = getInputAndProcess(board, currentTurn)
        displayThings(dummy_board, board)
        if evaluate(board, currentTurn, last_marked_position):
            print(f"Hurray! Player {currentTurn} wins the game.")
            break
        currentTurn = 3 - currentTurn
    else:
        print("Alas! Game tied.")

game()
