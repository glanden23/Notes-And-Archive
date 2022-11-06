#sampleBoard = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]

'''
for row in range(len(sampleBoard)):
    for columns in range(len(sampleBoard[row])):
        print(sampleBoard[row][columns])
'''

def printBoard(board):
    for r in range(len(board)):
        print(board[r][0]+"|"+board[r][1]+"|"+board[r][2])
        if r<len(board)-1:
            print("-"*5)

def catGame(board):
    for row in range(len(board)):
        for columns in range(len(board[row])):
            if (board[row][columns]) == " ":
                return False
    print("Cat game.")
    return True

def checkForWinners(board):
    for r in range(len(board)):
        if board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][0]!=" ":
            print("Winner winner, Turkey dinner!")
            return True
    for c in range(len(board)):
        if board[0][c] == board[1][c] == board[2][c] and board[0][c] != " ":
            print("Winner winner, Turkey dinner!")
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        print("Winner winner, Turkey dinner!")
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        print("Winner winner, Turkey dinner!")
        return True
    return False

def chooseSpot(r,c,symbol,board):
    if board[r][c] == " ":
        board[r][c]=symbol
        return True
    return False

board=[[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

symbol="X"
while symbol!="Q":
    printBoard(board)
    goodSpot=False
    while not goodSpot:
        r= int(input("row: "))-1
        c = int(input("col: "))-1
        if ((0<=r<=2) and (0<=c<=2)):
            if (not chooseSpot(r,c,symbol,board)):
                print("Spots Taken")
            else:
                goodSpot = True
    
    if symbol=="X":
        symbol="O"
    else:
        symbol="X"
    if (catGame(board) or checkForWinners(board)):
        symbol="Q"