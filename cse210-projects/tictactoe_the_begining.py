# Requirement 1 - The program must have a comment with assignment and author names
'''
Tic-Tac-Toe: Week 2 Solo Code TicTacToe( A work in progress)
Author: Jennifer Leon
'''
# Requirement 5 - The program must have a function called main
# Requirement 3 - The program must have at least one while loop.
# Requirement 4 - The program must have more than one function. - 7 functions
def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        print("Excellent Choice")
        player = next_player(player)
    display_board(board)
    print("Thats a wrap. Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    

def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
   square = int(input(f"{player}'s turn to choose a square (1-9): "))
   board[square - 1] = player


# Requirement 2 - The program must have at least one if/then block. - 3 if then statements
def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()