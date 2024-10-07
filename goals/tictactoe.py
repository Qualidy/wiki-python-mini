def print_tick_tack_toe_field(board):
    print(f"{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} | {board[5]}\n{board[6]} | {board[7]} | {board[8]}")

def add_tick(board, pos, tick):
    board[pos] = tick

def is_empty(board, pos):
    return board[pos] in [0, 1, 2, 3, 4, 5, 6, 7, 8]

def has_won(board):
    if board[0] == board[1] == board[2]:
        return board[0]
    if board[3] == board[4] == board[5]:
        return board[1]
    if board[6] == board[7] == board[8]:
        return board[2]
    if board[0] == board[3] == board[6]:
        return board[0]
    if board[1] == board[4] == board[7]:
        return board[1]
    if board[2] == board[5] == board[8]:
        return board[2]
    if board[0] == board[5] == board[8]:
        return board[0]
    if board[2] == board[5] == board[6]:
        return board[2]
    return False

def gameloop():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player1, player2 = 'X', 'O'
    current_player = player1
    while not has_won(board):
        print_tick_tack_toe_field(board)
        position = int(input(f"Spieler {current_player}, wo willst du setzen?"))

        if is_empty(board, position):
            add_tick(board, position, current_player)
        else:
            print("Die Stelle ist leider schon voll! Zug vergeudet!")

        # Wechsle Spieler
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

    print("Herzlichen Glückwunsch!")


if __name__ == '__main__':
    gameloop()