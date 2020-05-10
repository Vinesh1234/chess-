from player import switch_player
from pieces import *
from board import remaining_pieces, validate_move, create_new, update_board, show_board
from legal_moves import *


def checkmate(board, move_num, checking_pieces):
    if checking_pieces == 0:
        return False
    king_positions = king_possibilities(board, move_num)
    if check(board, move_num):
        if not controlled_squares(board, move_num + 1, checking_pieces[0]):
            return False
        for i in range(0, len(king_positions)):
            if validate_move(board, king_positions[i], move_num):
                if controlled_squares(board, move_num, king_positions[i]):
                    return False

    return True


def all_legal_moves(board, move_number, enpassant_square, king_count_w, king_count_b, rook_count_w_l, rook_count_w_r,
                    rook_count_b_l,
                    rook_count_b_r):
    legal_moves = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] != ".":
                start = [i + 1, j]
                piece = board[i][j]
                if move_number % 2 == 0:
                    if piece == "P":
                        legal_moves.append(legal_pawn_moves(board, start, move_number))
                        legal_moves.append(legal_en_passant(board, move_number, enpassant_square, start))
                    elif piece == "B":
                        legal_moves.append(legal_bishop_moves(board, start, move_number))
                    elif piece == "N":
                        legal_moves.append(legal_knight_moves(board, start, move_number))
                    elif piece == "Q":
                        legal_moves.append(legal_queen_moves(board, start, move_number))
                    elif piece == "R":
                        legal_moves.append(legal_rook_moves(board, start, move_number))
                    elif piece == "K":
                        legal_moves.append(legal_king_moves(start, board, move_number))
                elif move_number % 2 != 0:
                    if piece == "p":
                        legal_moves.append(legal_pawn_moves(board, start, move_number))
                        legal_moves.append(legal_en_passant(board, move_number, enpassant_square, start))
                    elif piece == "b":
                        legal_moves.append(legal_bishop_moves(board, start, move_number))
                    elif piece == "n":
                        legal_moves.append(legal_knight_moves(board, start, move_number))
                    elif piece == "q":
                        legal_moves.append(legal_queen_moves(board, start, move_number))
                    elif piece == "r":
                        legal_moves.append(legal_rook_moves(board, start, move_number))
                    elif piece == "k":
                        legal_moves.append(legal_king_moves(start, board, move_number))
    legal_moves = [i for i in legal_moves if i != []]
    final_legal_moves = []
    for i in legal_moves:
        if i not in final_legal_moves:
            final_legal_moves.append(i)
    if move_number % 2 == 0:
        if king_count_w == 0 and rook_count_w_r == 0 and not check(board, move_number) \
                and controlled_squares(board, move_number, [1, 5]) and controlled_squares(board, move_number, [1, 6]) \
                and validate_move(board, [1, 5], move_number) and validate_move(board, [1, 6], move_number):
            final_legal_moves.append("O-O")
        elif king_count_w == 0 and rook_count_w_l == 0 and not check(board, move_number) \
                and controlled_squares(board, move_number, [1, 3]) and controlled_squares(board, move_number, [1, 2]) \
                and validate_move(board, [1, 3], move_number) and validate_move(board, [1, 2], move_number):
            final_legal_moves.append("O-O-O")
    elif move_number % 2 != 0:
        if king_count_b == 0 and rook_count_b_l == 0 and not check(board, move_number) \
                and controlled_squares(board, move_number, [8, 5]) and controlled_squares(board, move_number, [8, 6]) \
                and validate_move(board, [8, 5], move_number) and validate_move(board, [8, 6], move_number):
            final_legal_moves.append("O-O")
        elif king_count_b == 0 and rook_count_b_r == 0 and not check(board, move_number) \
                and controlled_squares(board, move_number, [8, 3]) and controlled_squares(board, move_number, [8, 2]) \
                and validate_move(board, [8, 3], move_number) and validate_move(board, [8, 2], move_number):
            final_legal_moves.append("O-O-O")
    return final_legal_moves


def stalemate(legal_moves):
    if len(legal_moves) == 0:
        return True
    else:
        return False
