import time
import random
board=[[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
sampleBoard = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]

def clearScreen():
    for i in range(250):
        print(" ")

def printBoard():
    for i in board:
        print(" | ".join(i))
        print("----------")

def printSample():
    for i in range(len(sampleBoard)):
        print(" | ".join(sampleBoard[i]))
        if i < 2:
            print("-"*9)
            
def checkForWinner():
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != " ":
                count+=1
    if count == 9:
        print("!!! Tie !!!")
        exit()
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            print("!!! Winner !!!")
            exit()
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            print("!!! Winner !!!")
            exit()
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        print("!!! Winner !!!")
        exit()
    if board[0][2] == board[1][2] == board[2][1] and board[0][2] != " ":
        print("!!! Winner !!!")
        exit()

def computerInput(user):
    for row in range(len(board)):
        if board[row][0] == board[row][1] and board[row][0] != " ":
            return
    for col in range(len(board)):
        if board[0][col] == board[1][col] and board[0][col] != " ":
            return
    if board[0][0] == board[1][1] and board[0][0] != " ":
        return
    if board[0][2] == board[1][2] and board[0][2] != " ":
        return
    random1 = random.randint(0, 2)
    random2 = random.randint(0, 2)
    while board[random1][random2] != " ":
        random1 = random.randint(0, 2)
        random2 = random.randint(0, 2)
    board[random1][random2] = user
    sampleBoard[random1][random2] = user
        

def userInput(user):
    printSample()
    UI = input("(Q to quit) >>> ")
    if UI.lower() == "q":
        exit()
    while UI.isdigit() == False or int(UI) > 9 or int(UI) < 1:
        UI = input("(Q to quit) >>> ")
        if UI == "Q":
            exit()
    UI = int(UI)
    if UI <= 3:
        row = 0
        col = UI - 1
    elif UI <= 6:
        row = 1
        col = UI - 4
    else:
        row = 2
        col = UI - 7
    if board[row][col] != " ":
        clearScreen()
        print("ERROR: ALREADY TAKEN")
        userInput(user)
        return
    if user == "X":
        sampleBoard[row][col] = user
        board[row][col] = user
    else:
        sampleBoard[row][col] = user
        board[row][col] = user
    clearScreen()
    printBoard()
    time.sleep(2)

def playComputer():
    keepGoing=True
    while keepGoing:
        checkForWinner()
        clearScreen()
        userInput("X")
        checkForWinner()
        computerInput("O")
        checkForWinner()

def playSelf():
    keepGoing=True
    while keepGoing:
        checkForWinner()
        clearScreen()
        userInput("X")
        checkForWinner()
        clearScreen()
        userInput("O")
        checkForWinner()
        
if __name__ == "__main__":
    print("""
Welcome! What would you like to play?
1. Play Self (Player Vs. Player)
2. Against Computer (Player Vs. AI)
          """)
    UI = input(">>> ")
    while UI.isdigit() == False or int(UI) > 2 or int(UI) < 1:
        UI = input(">>> ")
    UI = int(UI)
    if UI == 1:
        playSelf()
    else:
        playComputer()