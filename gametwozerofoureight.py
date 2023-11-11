import copy 
from basicGameLogic import addNewValue, display, merge_down, merge_left, merge_right, merge_up, noMoves, won, board, boardSize


print("welcome to 2048 totally unique and not at all solen code from some torial")
display()

gameOver = False

while not gameOver:
    move = input("begin the mergin")

    validInput = True
    
    tempBoard = copy.deepcopy(board)

    if move == "2":
        board = merge_down(board)
    elif move == "6":
        board = merge_right(board) 
    elif move == "8":
        board == merge_up(board)
    elif move == "4":
        board == merge_left(board)
    elif move == "q":
        gameOver = True
        print("fair enough")
    else:
        validInput = False

    if not validInput:
        print("wrong input idiot")
    else:
        if board == tempBoard:
            display()
            print("MOREEE")
        else:
            if won():
                display()
                print("you won")
                gameOver = True
            else:
                addNewValue()
                display()
                if noMoves():
                    print("it seems there are no more moves left")
                    gameOver = True