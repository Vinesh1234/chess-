from player import switch_player
import numpy as np
from board import check_square, clear_path, validate_move


def pawn(board, start, end, move_number):
    if start == end:
        return False
    if switch_player(move_number):  # if it whites move
        if start[0] == 2 and start[1] == end[1]:  # when the pawn is making it's first move
            if (start[0] + 2 == end[0]) or (start[0] + 1 == end[0]):
                return True

        elif start[0] != 2 and start[1] == end[1] and check_square(board, end) == ".":
            # checking that if it isn't at starting position, only moves one square
            if start[0] + 1 == end[0]:
                return True
        elif start[1] != end[1] and check_square(board, end) != ".":  # capturing, changes column
            if (start[1] + 1 == end[1]) and start[0] + 1 == end[0]:
                if check_square(board, end) == ".":
                    return False
                else:
                    return True
            elif (start[1] - 1 == end[1]) and start[0] + 1 == end[0]:  # capturing, the other way
                if check_square(board, end) == ".":
                    return False
                else:
                    return True
        else:
            return False


    elif not switch_player(move_number):  # if it is blacks move
        if start[0] == 7 and start[1] == end[1]:
            if (start[0] - 2 == end[0]) or (start[0] - 1 == end[0]):
                return True

        elif start[0] != 7 and start[1] == end[1] and check_square(board, end) == ".":
            # checking that if it isn't at starting position, only moves one square
            if start[0] - 1 == end[0]:
                return True

        elif start[1] != end[1] and check_square(board, end) != ".":  # capturing, changes column
            if (start[1] + 1 == end[1]) and start[0] - 1 == end[0]:
                if check_square(board, end) == ".":
                    return False
                else:
                    return True
            elif (start[1] - 1 == end[1]) and start[0] - 1 == end[0]:  # capturing, the other way
                if check_square(board, end) == ".":
                    return False
                else:
                    return True
        else:
            return False


def knight(start, end):
    if start == end:
        return False
    if start[1] + 2 == end[1] and ((start[0] + 1) == end[0] or (start[0] - 1 == end[0])):  # Horizontal, right
        return True
    elif start[1] - 2 == end[1] and ((start[0] + 1) == end[0] or (start[0] - 1 == end[0])):  # Horizontal, left
        return True
    elif start[1] + 1 == end[1] and (start[0] + 2 == end[0] or (start[0] - 2 == end[0])):  # vertical, right
        return True
    elif start[1] - 1 == end[1] and (start[0] + 2 == end[0] or (start[0] - 2 == end[0])):  # vertical, left
        return True
    else:
        return False


def king(start, end):
    if start == end:
        return False
    if (start[0] + 1 == end[0] or start[0] - 1 == end[0]) and (start[1] + 1 == end[1] or start[1] - 1 == end[1]):
        #  this takes into account diag moves
        return True
    elif (start[0] + 1 == end[0] or start[0] - 1 == end[0]) and (start[1] == end[1]):
        return True
    elif (start[0] == end[0]) and (start[1] - 1 == end[1] or start[1] + 1 == end[1]):
        return True
    else:
        return False


def bishop(board, start, end):
    if start == end:
        return False
    x_dir = np.sign(end[1] - start[1])  # Direction of letters
    y_dir = np.sign(end[0] - start[0])  # Direction of numbers
    if abs(end[1] - start[1]) != abs(end[0] - start[0]):
        return False
    elif abs(end[1] - start[1]) == abs(end[0] - start[0]):
        for i in range(1, abs(end[1] - start[1])):
            if not clear_path(board, start[0] + (i * y_dir), start[1] + (i * x_dir)):
                return False
        return True

    else:
        return False


def rook(board, start, end):
    if start == end:
        return False
    y_dir = np.sign(end[0] - start[0])
    x_dir = np.sign(end[1] - start[1])
    if start[1] == end[1] and abs(start[0] - end[0]) >= 0:
        for i in range(1, abs((start[0] - end[0]))):
            if not clear_path(board, start[0] + (i * y_dir), start[1]):
                return False
        return True

    elif start[1] != end[1] and start[0] == end[0]:
        for i in range(1, abs((start[1] - end[1]))):
            if not clear_path(board, start[0], start[1] + (i * x_dir)):
                return False
        return True

    else:
        return False


def queen(board, start, end):
    if start == end:
        return False
    if rook(board, start, end) or bishop(board, start, end):
        return True
    else:
        return False


def controlled_squares(board, move_number, king_end):
    """If the enemy piece CAN move to the "king_end" square, it will return FALSE"""
    if switch_player(move_number):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if 97 <= ord(board[i][j]) <= 122:
                    start = [i + 1, j]
                    piece = chr(ord(board[i][j]))
                    if piece == "p":
                        if (start[1] + 1 == king_end[1]) and start[0] - 1 == king_end[0]:
                            return False
                        elif (start[1] - 1 == king_end[1]) and start[0] - 1 == king_end[0]:
                            return False
                    elif piece == "n":
                        if knight(start, king_end):
                            return False
                    elif piece == "b":
                        if bishop(board, start, king_end):
                            return False
                    elif piece == "q":
                        if queen(board, start, king_end):
                            return False
                    elif piece == "r":
                        if rook(board, start, king_end):
                            return False
                    elif piece == "k":
                        if king(start, king_end):
                            return False
        return True
    if not switch_player(move_number):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if 65 <= ord(board[i][j]) <= 90:
                    start = [i + 1, j]
                    piece = chr(ord(board[i][j]))
                    # print("starting pos:", start, "piece:", piece)
                    if piece == "P":
                        if (start[1] + 1 == king_end[1]) and start[0] + 1 == king_end[0]:
                            return False
                        elif (start[1] - 1 == king_end[1]) and start[0] + 1 == king_end[0]:
                            return False
                    elif piece == "N":
                        if knight(start, king_end):
                            return False
                    elif piece == "B":
                        if bishop(board, start, king_end):
                            return False
                    elif piece == "Q":
                        if queen(board, start, king_end):
                            return False
                    elif piece == "R":
                        if rook(board, start, king_end):
                            return False
                    elif piece == "K":
                        if king(start, king_end):
                            return False
        return True


def pieces_controlled_squares(board, move_number):
    """returns the pieces checking the king"""
    pieces_white = []
    pieces_black = []
    king_end = king_position(board, move_number)
    if switch_player(move_number):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if 97 <= ord(board[i][j]) <= 122:
                    start = [i + 1, j]
                    piece = chr(ord(board[i][j]))
                    # print("starting pos:", start, "piece:", piece)
                    if piece == "p":
                        if (start[1] + 1 == king_end[1]) and start[0] - 1 == king_end[0]:
                            pieces_black.append(start)
                        elif (start[1] - 1 == king_end[1]) and start[0] - 1 == king_end[0]:
                            pieces_black.append(start)
                    elif piece == "n":
                        if knight(start, king_end):
                            pieces_black.append(start)
                    elif piece == "b":
                        if bishop(board, start, king_end):
                            pieces_black.append(start)
                    elif piece == "q":
                        if queen(board, start, king_end):
                            pieces_black.append(start)
                    elif piece == "r":
                        if rook(board, start, king_end):
                            pieces_black.append(start)
                    elif piece == "k":
                        if king(start, king_end):
                            pieces_black.append(start)
        return pieces_black
    if not switch_player(move_number):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if 65 <= ord(board[i][j]) <= 90:
                    start = [i + 1, j]
                    piece = chr(ord(board[i][j]))
                    # print("starting pos:", start, "piece:", piece)
                    if piece == "P":
                        if (start[1] + 1 == king_end[1]) and start[0] + 1 == king_end[0]:
                            pieces_white.append(start)
                        elif (start[1] - 1 == king_end[1]) and start[0] + 1 == king_end[0]:
                            pieces_white.append(start)
                    elif piece == "N":
                        if knight(start, king_end):
                            pieces_white.append(start)
                    elif piece == "B":
                        if bishop(board, start, king_end):
                            pieces_white.append(start)
                    elif piece == "Q":
                        if queen(board, start, king_end):
                            pieces_white.append(start)
                    elif piece == "R":
                        if rook(board, start, king_end):
                            pieces_white.append(start)
                    elif piece == "K":
                        if king(start, king_end):
                            pieces_white.append(start)
        return pieces_white


def king_position(board, move_number):
    if switch_player(move_number):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == "K":
                    position = [i + 1, j]
                    return position
    if not switch_player(move_number):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == "k":
                    position = [i + 1, j]
                    return position


def check(board, move_num):
    # king_position() will account for white and black
    king_pos = king_position(board, move_num)
    if not controlled_squares(board, move_num, king_pos):
        return True
    else:
        return False


def promotion(board, start, end, final_piece):
    row = end[0]
    column = end[1]
    row_start = start[0]
    column_start = start[1]
    board[row - 1][column] = final_piece
    board[row_start - 1][column_start] = "."


def can_en_passant(board, en_passant_square, end, start, move_number):
    if en_passant_square == 0:
        return False
    if switch_player(move_number):
        if start[1] != end[1] and start[0] + 1 == end[0] and check_square(board,
                                                                          end) == "." and end == en_passant_square:
            return True
    elif not switch_player(move_number):
        if start[1] != end[1] and start[0] - 1 == end[0] and check_square(board,
                                                                          end) == "." and end == en_passant_square:
            return True


def execute_enpassant(board, start, end, move_number):
    if switch_player(move_number):
        board[end[0] - 1][end[1]] = board[start[0] - 1][start[1]]
        board[start[0] - 1][start[1]] = "."
        board[end[0] - 2][end[1]] = "."
    elif not switch_player(move_number):
        board[end[0] - 1][end[1]] = board[start[0] - 1][start[1]]
        board[start[0] - 1][start[1]] = "."
        board[end[0]][end[1]] = "."


def castle(board, move, move_number, king_count_w, king_count_b, rook_count_w_l, rook_count_w_r, rook_count_b_l,
           rook_count_b_r):
    if switch_player(move_number):
        if move == "O-O" and king_count_w == 0 and rook_count_w_r == 0 and not check(board, move_number) \
                and controlled_squares(board, move_number, [1, 5]) and controlled_squares(board, move_number, [1, 6])\
                and validate_move(board, [1, 5], move_number) and validate_move(board, [1, 6], move_number):
            board[0][5] = board[0][7]
            board[0][6] = board[0][4]
            board[0][4] = "."
            board[0][7] = "."

        elif move == "O-O-O" and king_count_w == 0 and rook_count_w_l == 0 and not check(board, move_number) \
                and controlled_squares(board, move_number, [1, 3]) and controlled_squares(board, move_number, [1, 2]) \
                and validate_move(board, [1, 3], move_number) and validate_move(board, [1, 2], move_number):
            board[0][3] = board[0][0]
            board[0][2] = board[0][4]
            board[0][4] = "."
            board[0][0] = "."

    elif not switch_player(move_number):
        if move == "O-O" and king_count_b == 0 and rook_count_b_l == 0 and not check(board, move_number) \
                and controlled_squares(board, move_number, [8, 5]) and controlled_squares(board, move_number, [8, 6]) \
                and validate_move(board, [8, 5], move_number) and validate_move(board, [8, 6], move_number):
            board[7][5] = board[7][7]
            board[7][6] = board[7][4]
            board[7][4] = "."
            board[7][7] = "."

        elif move == "O-O-O" and king_count_b == 0 and rook_count_b_r == 0 and not check(board, move_number) \
                and controlled_squares(board, move_number, [8, 3]) and controlled_squares(board, move_number, [8, 2]) \
                and validate_move(board, [8, 3], move_number) and validate_move(board, [8, 2], move_number):
            board[7][2] = board[7][4]
            board[7][3] = board[7][0]
            board[7][4] = "."
            board[7][0] = "."
