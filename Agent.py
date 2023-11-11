import copy 
from basicGameLogic import addNewValue, display, merge_down, merge_left, merge_right, merge_up, noMoves, won, board, boardSize

# def heuristic_score(board):
#     # Prioritize higher values in specific positions
#     score = 0

#     # Define the desired order of positions
#     desired_positions = [(boardSize - 1, 0), (boardSize - 1, 1), (boardSize - 1, 2), (boardSize - 1, 3)]

#     for i, j in desired_positions:
#         score += board[i][j]

#     return score

# def generate_possible_moves(board):
#     moves = []
#     possible_moves = [2,4,8,6]

#     for move in possible_moves:
#         temp_board = copy.deepcopy(board)

#         if move == 2:
#             temp_board = merge_down(temp_board)
#         elif move == 4:
#             temp_board = merge_left(temp_board)
#         elif move == 6:
#             temp_board = merge_right(temp_board)
#         elif move == 8:
#             temp_board = merge_up(temp_board)

#         # Check if the move resulted in a different board state
#         if temp_board != board:
#             moves.append(move)

#     return moves

# def make_best_move(board):
#     best_move = None
#     best_score = 10  # Initialize with negative infinity

#     for move in generate_possible_moves(board):
#         temp_board = copy.deepcopy(board)
#         temp_board = simulate_move(temp_board, move)  # Implement a function to simulate the move
#         score = heuristic_score(temp_board)
        
#         if score > best_score:
#             best_score = score
#             best_move = move

#     return best_move if best_move is not None else "2"  # Return a default move if no valid moves are found

def simulate_move(board, move):
    temp_board = copy.deepcopy(board)

    if move == "2":
        temp_board = merge_down(temp_board)
    elif move == "6":
        temp_board = merge_right(temp_board)
    elif move == "8":
        temp_board = merge_up(temp_board)
    elif move == "4":
        temp_board = merge_left(temp_board)

    return temp_board

board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

gameOver = False
move = "2"  # Initialize move here

for i in range(5):
    print("Current Board:")
    display()
    print("Chosen Move:", move)
    temp_board = copy.deepcopy(board)
    temp_board = simulate_move(temp_board, move)
    if temp_board != board:
        board = temp_board
        addNewValue()
        display()
        if won():
            display()
            print("You won!")
            gameOver = True
        elif noMoves():
            print("It seems there are no more moves left.")
            gameOver = True
    move = "2" # make_best_move(board)  # Move the assignment inside the loop
