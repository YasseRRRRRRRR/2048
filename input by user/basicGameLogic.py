import random
import copy

boardSize = 4

def display():
    # finding biggest number
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpace = len(str(largest))

    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += " " * numSpace + "|"
            else:
                currRow += (" " * (numSpace - len(str(element)))) + str(element) + "|"

        print(currRow)
    print()

def mergeOneRowL(row):
    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0, -1):
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
    for i in range(boardSize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0

    for i in range(boardSize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row


def merge_left(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])
    return currentBoard


def reverse(row):
    new = []
    for i in range(boardSize - 1, -1, -1):
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


def initialize_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        board.append(row)

    num_needed = 2

    while num_needed > 0:
        row_num = random.randint(0, size - 1)
        col_num = random.randint(0, size - 1)

        if board[row_num][col_num] == 0:
            board[row_num][col_num] = pickNewValue()
            num_needed -= 1

    return board


def won():
    for row in board:
        if 2048 in row:
            return True
    return False


def noMoves():
    temp_board1 = copy.deepcopy(board)
    temp_board2 = copy.deepcopy(board)

    temp_board1 = merge_down(temp_board1)
    if temp_board1 == temp_board2:
        temp_board1 = merge_left(temp_board1)
        if temp_board1 == temp_board2:
            temp_board1 = merge_right(temp_board1)
            if temp_board1 == temp_board2:
                temp_board1 = merge_up(temp_board1)
                if temp_board1 == temp_board2:
                    return True
    else:
        return False


# Initialize the board
board = initialize_board(boardSize)
