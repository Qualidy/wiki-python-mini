def print_tick_tack_toe_field(board):
    print(f"{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} | {board[5]}\n{board[6]} | {board[7]} | {board[8]}\n")

def add_tick(board, pos, tick):
    board[pos] = tick

def has_won(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[5] == board[8] or
            board[2] == board[5] == board[6])

def gameloop():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    current_player = 'X'
    next_player = '0'

    while not has_won(board):
        print_tick_tack_toe_field(board)
        position = int(input(f"Spieler {current_player}, wo willst du setzen?"))

        add_tick(board, position, current_player)

        # Wechsle Spieler
        zwischenspeicher = current_player
        current_player = next_player
        next_player = zwischenspeicher

    print(f"Herzlichen Glückwunsch {next_player}!")


if __name__ == '__main__':
    gameloop()