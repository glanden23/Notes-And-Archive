import time, random
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
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        print("!!! Winner !!!")
        exit()

def computerInput(user):
    if board[1][1] == " ":
        sampleBoard[1][1] = user
        board[1][1] = user
        return
    for row in range(len(board)):
        count = 0
        for i in board[row]:
            if i != user and i != " ":
                count+=1
        if count == 2:
            if not user in board[row]:
                index = board[row].index(" ")
                sampleBoard[row][index] = user
                board[row][index] = user
                return
    for row in range(len(board) - 1):
        for col in range(len(board[row])):
            if board[row+1][col] == board[row][col] and board[row][col] != " ":
                for i in range(3):
                    if board[i][col] == " ":
                        sampleBoard[i][col] = user
                        board[i][col] = user
                        return
    if board[0][0] == board[1][1] and board[0][0] != " " and board[0][0] != user:
        if board[2][2] != user:
            board[2][2] = user
            sampleBoard[2][2] = user
            return
    if board[1][1] == board[2][2] and board[1][1] != " " and board[1][1] != user:
        if board[0][0] != user:
            board[0][0] = user
            sampleBoard[0][0] = user
            return
    if board[0][0] == board[2][2] and board[0][0] != " " and board[0][0] != user:
        if board[1][1] != user:
            board[1][1] = user
            sampleBoard[1][1] = user
            return
    if board[0][2] == board[1][1] and board[0][2] != " " and board[0][2] != user:
        if board[2][0] != user:
            board[2][0] = user
            sampleBoard[2][0] = user
            return
    if board[1][1] == board[2][0] and board[1][1] != " " and board[1][1] != user:
        if board[0][2] != user:
            board[0][2] = user
            sampleBoard[0][2] = user
            return
    if board[0][2] == board[2][0] and board[0][2] != " " and board[0][2] != user:
        if board[1][1] != user:
            board[1][1] = user
            sampleBoard[1][1] = user
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

def CPUvsCPU():
    keepGoing=True
    while keepGoing:
        computerInput("X")
        printBoard()
        checkForWinner()
        time.sleep(2)
        clearScreen()
        computerInput("O")
        printBoard()
        checkForWinner()
        time.sleep(2)
        clearScreen()

def playComputer():
    keepGoing=True
    while keepGoing:
        checkForWinner()
        clearScreen()
        userInput("X")
        checkForWinner()
        computerInput("O")
        printBoard()
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
3. Computer Vs. Computer
4. Computer Vs. Computer (FAST)
          """)
    UI = input(">>> ")
    while UI.isdigit() == False or int(UI) > 4 or int(UI) < 1:
        UI = input(">>> ")
    UI = int(UI)
    if UI == 1:
        playSelf()
    elif UI == 2:
        playComputer()
    else:
        CPUvsCPU()
        