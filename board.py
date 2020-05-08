from player import switch_player


def create_new():
    board = [["R", "N", "B", "Q", "K", "B", "N", "R"], ["P" for i in range(0, 8)]]
    for i in range(0, 4):
        board.append(["." for i in range(0, 8)])
    board.append(["p" for i in range(0, 8)])
    board.append(["r", "n", "b", "q", "k", "b", "n", "r"])
    return board


def update_board(board, start, end):
    initial_row = start[0]
    initial_column = start[1]
    row = end[0]
    column = end[1]
    board[int(row) - 1][column] = board[int(initial_row) - 1][initial_column]
    board[int(initial_row) - 1][initial_column] = "."


def show_board(board):
    for i in range(len(board) - 1, -1, -1):
        a = ' '.join(board[i])
        print(a)


def check_square(board, square):
    if not (1 <= square[0] <= 8 and 0 <= square[1] <= 7):
        return False
    return board[square[0] - 1][square[1]]


def clear_path(board, row, column):
    if board[row - 1][column] == ".":
        return True
    else:
        return False


def retract_move(board, start, end, initial_piece):
    board[start[0] - 1][start[1]] = board[end[0] - 1][end[1]]
    board[end[0] - 1][end[1]] = initial_piece


def remaining_pieces(board, color):
    remaining_black = []
    remaining_white = []
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if 97 <= ord(board[i][j]) <= 122:
                remaining_black.append(board[i][j])
            elif 65 <= ord(board[i][j]) <= 90:
                remaining_white.append(board[i][j])
    if color == "black":
        return remaining_black
    elif color == "white":
        return remaining_white


def validate_move(board, end, move_number):
    """ This function makes sure that you can't capture your own piece"""
    if not (1 <= end[0] <= 8 and 0 <= end[1] <= 7):
        return False

    if switch_player(move_number):
        piece = find_piece(board, end)
        if piece == ".":
            return True
        elif 65 <= ord(piece) <= 90:
            return False
        else:
            return True

    elif not switch_player(move_number):
        piece = find_piece(board, end)
        if piece == ".":
            return True
        elif 97 <= ord(piece) <= 122:
            return False
        else:
            return True


def find_piece(board, start):
    column = start[1]
    row = start[0]
    piece = board[int(row) - 1][int(column)]
    return piece


