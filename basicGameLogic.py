import random
import copy

boardSize = 4
def display():
    #finding bigguest number
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpace = len(str(largest))

    for row in board:
        currRow = "|"
        pluses = ""
        for element in row:
            if element == 0:
                currRow += " "*numSpace +"|"           
            else:
                currRow += (" "*(numSpace - len(str(element)))) + str(element)+"|"
            
        print(currRow)
    print()

def mergeOneRowL(row):  
    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0 , -1):
            if  row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
    for i in range(boardSize - 1):
        if  row[i] == row[i+1]:
            row[i] *=2
            row[i+1] = 0

    for i in range(boardSize - 1, 0, -1):
        if  row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    return row


def merge_left(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])
    return currentBoard


def reverse(row):
    new = []
    for i in range(boardSize -1, -1, -1):
        new.append(row[i])
    return new

def merge_right(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard

def transpose(currenBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currenBoard[j][i]
                currenBoard[j][i] = currenBoard[i][j]
                currenBoard[i][j] = temp
    return currenBoard

def merge_up(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def merge_down(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def pickNewValue():
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2

def addNewValue():
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    while not board[rowNum][colNum] == 0:
        rowNum = random.randint(0, boardSize - 1)
        colNum = random.randint(0, boardSize - 1)
    board[rowNum][colNum] = pickNewValue()

def won():
    for row in board:
        if 2048 in row:
            return True
    return False

def noMoves():
    tempBoard1 = copy.deepcopy(board)
    tempBoard2 = copy.deepcopy(board)

    tempBoard1 = merge_down(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_left(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempBoard1 = merge_right(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = merge_up(tempBoard1)
                if tempBoard1 == tempBoard2:
                    return True
    else:
        return False

board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)


numNeeded = 2

while numNeeded > 0:
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numNeeded -= 1

    