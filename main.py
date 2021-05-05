import random

from Board import layout

MY_SEPARATOR = "=" * 50


def main() -> None:
    #Invitation & Rulles
    invitation_and_rulles()

    # Creation board with defined size
    muj_board, size_of_board = Board()

    # Displaying board
    if size_of_board in layout.keys():
        print(layout[size_of_board ])

    #Selection of symbol
    Symbol_player1 = Selection_of_X_0()
    player = 1
    while True:
        print(f"Player {player} turn:")
        move_row, board = Players_move_row(muj_board,size_of_board, player)
        move_column, board = Players_move_column(muj_board,size_of_board, player)
        player, board = Print_move(muj_board, move_row, move_column, Symbol_player1, player)
        print(board)





def invitation_and_rulles() -> None:
    """ Invitation function."""
    print(MY_SEPARATOR)
    print("Welcome to Tic Tac Toe game".center(50))
    print(MY_SEPARATOR)
    print(f'GAME RULES:'.center(50))
    print("""
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in one of the possible direction:
    * horizontal
    * vertical
    * diagonal
    """)
    print(MY_SEPARATOR)
    print("Let's start the game.".center(50))
    print(MY_SEPARATOR)



def Board() -> (list,int):
    """Layout of the board"""

    # size of the board
    while True:
        size_of_board = input("Please enter size of the board e.g.'3','4','5' for 3x3, 4x4, 5x5 board size: ")
        if size_of_board.isalpha():
            continue
        elif int(size_of_board) > 5 or int(size_of_board) < 3:
            continue
        break
    size_of_board = int(size_of_board)

    muj_board = []
    for row in range(size_of_board):
        muj_board.append([""]*size_of_board)

    return muj_board, size_of_board


def Selection_of_X_0() -> str:
    while True:
        selection = input("Please select the corresponding symbol (X/0): ").upper()
        if selection == "X":
            return selection
        elif selection == "0":
            return selection


def Players_move_row(muj_board, size_of_board, player):
    while True:
        print(MY_SEPARATOR)
        move_row = input(f"Player {player} | Please enter the row: ")
        if Control_of_user_input(move_row, size_of_board) == True:
            continue
        else:
            break
    return move_row, muj_board

def Players_move_column(muj_board, size_of_board, player):
    while True:
        print(MY_SEPARATOR)
        move_column = input(f"Player {player} | Please enter the column: ")
        if Control_of_user_input(move_column, size_of_board) == True:
            continue
        else:
            break
    return move_column, muj_board

def Control_of_user_input(User_move, size_of_board) ->bool:
    if User_move.isdigit():
        if int(User_move) < 0 or int(User_move) > (size_of_board-1):
            print(f"Your input {User_move} needs to be the digit from the list: {list(range(size_of_board))}")
            return True
        else:
            return False
    else:
        print(f"Your input {User_move} needs to be the digit {list(range(size_of_board))}")
        return True

def Print_move(muj_board, move_row, move_column, symbol, player):
    """ """
    print(MY_SEPARATOR)
    if player == 1:
        muj_board[int(move_row)][int(move_column)] = symbol
        player = 2

    else:
        if symbol == "X":
            muj_board[int(move_row)][int(move_column)] = "0"
            player = 1

        elif symbol == "0":
            muj_board[int(move_row)][int(move_column)] = "X"
            player = 1


    return player, muj_board



main()