#
#   Program:    TicTacToe.py
#   Author:     Samuel Osorio
#   Purpose:    Game tic tac toe
#


def main():
    TicTacToe = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possibilities = {
        1:[0, 1, 2],
        2:[3, 4, 5],
        3:[6, 7, 8],
        4:[0, 3, 6],
        5:[1, 4, 7],
        6:[2, 5, 8],
        7:[0, 4, 8],
        8:[2, 4, 6]
    }
    sign = "x"
    turn = 0
    print_board(TicTacToe)
    while turn < 9:
        square = int(input(f"{sign}'s turn to chose a square (1-9): "))
        if TicTacToe[square-1] != "x" and TicTacToe[square-1] != "o": 
            TicTacToe[square-1] = sign
            if sign == "x":
                sign = "o"
            else:
                sign = "x"
            print_board(TicTacToe)
            any_winner = verify(TicTacToe, possibilities)
            if any_winner != "No":
                print(f"####### Winner: {any_winner}'s #######")
                turn=8
            turn += 1
        else:
            print("\nwrong choice!!!!!!!!! try again!!!!!\n")
            print_board(TicTacToe)
    print("\nGood game. Thanks for playing!\n")


def print_board(board):
    separation = "-+-+-"
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(separation)
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(separation)
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def verify(choices, possibilities):
    winner = "No"
    for i in range(8):
        to_win = possibilities[i+1]
        option1 = to_win[0]
        option2 = to_win[1]
        option3 = to_win[2]
        if choices[option1] == choices[option2] and choices[option2] == choices[option3]:
            winner = choices[option1]
    return winner

if __name__ == "__main__":
    main()
