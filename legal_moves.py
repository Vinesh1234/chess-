from player import switch_player
from board import *
from pieces import *


def king_possibilities(board, move_number):
    position = king_position(board, move_number)
    position2 = [position[0] - 1, position[1]]
    position3 = [position[0] + 1, position[1]]
    position4 = [position[0] - 1, position[1] - 1]
    position5 = [position[0] + 1, position[1] + 1]
    position6 = [position[0] - 1, position[1] + 1]
    position7 = [position[0] + 1, position[1] - 1]
    position8 = [position[0], position[1] - 1]
    position9 = [position[0], position[1] + 1]
    positions = [position2, position3, position4, position5, position6, position7, position8, position9]
    for i in positions:
        if 0 >= i[0] or i[0] > 8:
            positions.remove(i)
        elif 0 >= i[1] or i[1] >= 8:
            positions.remove(i)
    return positions


def legal_pawn_moves(board, start, move_number):
    test_board = board.copy()
    pawn_moves_w = []
    pawn_moves_b = []
    if switch_player(move_number):
        if start[0] == 2:
            if check_square(board, [start[0] + 1, start[1]]) == ".":
                pawn_moves_w.append((start[0] + 1, start[1]))
                if check_square(board, [start[0] + 2, start[1]]) == ".":
                    pawn_moves_w.append((start[0] + 2, start[1]))
        elif start[0] != 2:
            if check_square(board, [start[0] + 1, start[1]]) == "." and start[0] + 1 <= 8:
                pawn_moves_w.append((start[0] + 1, start[1]))

        if check_square(board, [start[0] + 1, start[1] - 1]):
            if 97 <= ord(check_square(board, [start[0] + 1, start[1] - 1])) <= 122 and 0 <= start[1] - 1 <= 8 \
                    and start[0] + 1 <= 8:
                pawn_moves_w.append((start[0] + 1, start[1] - 1))
        if check_square(board, [start[0] + 1, start[1] + 1]):
            if 97 <= ord(check_square(board, [start[0] + 1, start[1] + 1])) <= 122 and 0 <= start[1] + 1 <= 8 \
                    and start[0] + 1 <= 8:
                pawn_moves_w.append((start[0] + 1, start[1] + 1))
        if check(board, move_number):
            new_legal_moves = []
            for i in range(0, len(pawn_moves_w)):
                initial_piece = find_piece(board, pawn_moves_w[i])
                update_board(test_board, start, pawn_moves_w[i])
                if not check(test_board, move_number):
                    new_legal_moves.append(pawn_moves_w[i])
                    retract_move(test_board, start, pawn_moves_w[i], initial_piece)
                else:
                    retract_move(test_board, start, pawn_moves_w[i], initial_piece)
            # print("pawn", new_legal_moves)
            return new_legal_moves
        final_list = filter_check(test_board, move_number, pawn_moves_w, start)
        # print("pawn", final_list)
        return final_list

    if not switch_player(move_number):
        if start[0] == 7:
            if check_square(board, [start[0] - 1, start[1]]) == ".":
                pawn_moves_b.append((start[0] - 1, start[1]))
                if check_square(board, [start[0] - 2, start[1]]) == ".":
                    pawn_moves_b.append((start[0] - 2, start[1]))
        elif start[0] != 7:
            if check_square(board, [start[0] - 1, start[1]]) == "." and start[0] - 1 >= 1:
                pawn_moves_b.append((start[0] - 1, start[1]))
        if check_square(board, (start[0] - 1, start[1] - 1)):
            if 65 <= ord(check_square(board, [start[0] - 1, start[1] - 1])) <= 90 and 0 <= start[1] - 1 <= 8 \
                    and start[0] - 1 >= 1:
                pawn_moves_b.append((start[0] - 1, start[1] - 1))
        if check_square(board, (start[0] - 1, start[1] + 1)):
            if 65 <= ord(check_square(board, [start[0] - 1, start[1] + 1])) <= 90 and 0 <= start[1] + 1 <= 8 \
                    and start[0] - 1 >= 1:
                pawn_moves_b.append((start[0] - 1, start[1] + 1))
        if check(board, move_number):
            new_legal_moves = []
            for i in range(0, len(pawn_moves_b)):
                initial_piece = find_piece(board, pawn_moves_b[i])
                update_board(test_board, start, pawn_moves_b[i])
                if not check(test_board, move_number):
                    new_legal_moves.append(pawn_moves_b[i])
                    retract_move(board, start, pawn_moves_b[i], initial_piece)
                else:
                    retract_move(test_board, start, pawn_moves_b[i], initial_piece)
            # print("pawn", new_legal_moves)
            return new_legal_moves
        final_list = filter_check(test_board, move_number, pawn_moves_b, start)
        # print("pawn", final_list)
        return final_list


def legal_knight_moves(board, start, move_number):
    legal_knight_w = []
    legal_knight_b = []
    test_board = board.copy()
    if switch_player(move_number):
        if validate_move(board, [start[0] + 1, start[1] + 2], move_number):
            legal_knight_w.append((start[0] + 1, start[1] + 2))
        if validate_move(board, [start[0] + 1, start[1] - 2], move_number):
            legal_knight_w.append((start[0] + 1, start[1] - 2))
        if validate_move(board, [start[0] - 1, start[1] - 2], move_number):
            legal_knight_w.append((start[0] - 1, start[1] - 2))
        if validate_move(board, [start[0] - 1, start[1] + 2], move_number):
            legal_knight_w.append((start[0] - 1, start[1] + 2))
        if validate_move(board, [start[0] + 2, start[1] - 1], move_number):
            legal_knight_w.append((start[0] + 2, start[1] - 1))
        if validate_move(board, [start[0] + 2, start[1] + 1], move_number):
            legal_knight_w.append((start[0] + 2, start[1] + 1))
        if validate_move(board, [start[0] - 2, start[1] + 1], move_number):
            legal_knight_w.append((start[0] - 2, start[1] + 1))
        if validate_move(board, [start[0] - 2, start[1] - 1], move_number):
            legal_knight_w.append((start[0] - 2, start[1] - 1))
        if check(board, move_number):
            new = filter_check(test_board, move_number, legal_knight_w, start)
            # print("knight", new)
            return new
        final_list = filter_check(test_board, move_number, legal_knight_w, start)
        # print("knight", final_list)
        return final_list
    if not switch_player(move_number):
        if validate_move(board, [start[0] + 1, start[1] + 2], move_number):
            legal_knight_b.append((start[0] + 1, start[1] + 2))
        if validate_move(board, [start[0] + 1, start[1] - 2], move_number):
            legal_knight_b.append((start[0] + 1, start[1] - 2))
        if validate_move(board, [start[0] - 1, start[1] - 2], move_number):
            legal_knight_b.append((start[0] - 1, start[1] - 2))
        if validate_move(board, [start[0] - 1, start[1] + 2], move_number):
            legal_knight_b.append((start[0] - 1, start[1] + 2))
        if validate_move(board, [start[0] + 2, start[1] - 1], move_number):
            legal_knight_b.append((start[0] + 2, start[1] - 1))
        if validate_move(board, [start[0] + 2, start[1] + 1], move_number):
            legal_knight_b.append((start[0] + 2, start[1] + 1))
        if validate_move(board, [start[0] - 2, start[1] + 1], move_number):
            legal_knight_b.append((start[0] - 2, start[1] + 1))
        if validate_move(board, [start[0] - 2, start[1] - 1], move_number):
            legal_knight_b.append((start[0] - 2, start[1] - 1))
        if check(board, move_number):
            new = filter_check(test_board, move_number, legal_knight_b, start)
            # print("knight", new)
            return new
        final_list_b = filter_check(test_board, move_number, legal_knight_b, start)
        # print("knight", final_list_b)
        return final_list_b


def legal_bishop_moves(board, start, move_number):
    bishop_moves_w = []
    bishop_moves_b = []
    test_board = board.copy()
    for i in range(1, 8):
        if not validate_move(board, [start[0] + (i * -1), start[1] + (i * 1)], move_number):
            break
        else:
            if move_number % 2 == 0:
                bishop_moves_w.append((start[0] + (i * -1), start[1] + (i * 1)))
            else:
                bishop_moves_b.append((start[0] + (i * -1), start[1] + (i * 1)))
    for j in range(1, 8):
        if not validate_move(board, [start[0] + (j * 1), start[1] + (j * 1)], move_number):
            break
        else:
            bishop_moves_w.append((start[0] + (j * 1), start[1] + (j * 1)))
    for i in range(1, 8):
        if not validate_move(board, [start[0] + (i * (-1)), start[1] + (i * -1)], move_number):
            break
        else:
            if move_number % 2 == 0:
                bishop_moves_w.append((start[0] + (i * (-1)), start[1] + (i * -1)))
            else:
                bishop_moves_b.append((start[0] + (i * (-1)), start[1] + (i * -1)))
    for i in range(1, 8):
        if not validate_move(board, [start[0] + (i * 1), start[1] + (i * -1)], move_number):
            break
        else:
            if move_number % 2 == 0:
                bishop_moves_w.append((start[0] + (i * 1), start[1] + (i * -1)))
            else:
                bishop_moves_b.append((start[0] + (i * 1), start[1] + (i * -1)))

    if move_number % 2 == 0:
        if check(board, move_number):
            new = filter_check(test_board, move_number, bishop_moves_w, start)
            # print("bishop", new)
            return new
        final_list = filter_check(test_board, move_number, bishop_moves_w, start)
        # print("bishop", final_list)
        return final_list
    else:
        if check(board, move_number):
            new = filter_check(test_board, move_number, bishop_moves_b, start)
            # print("bishop", new)
            return new
        final_list = filter_check(test_board, move_number, bishop_moves_b, start)
        # print("bishop", final_list)
        return final_list


def legal_rook_moves(board, start, move_number):
    rook_moves_w = []
    rook_moves_b = []
    test_board = board.copy()
    for i in range(1, 8):
        if not validate_move(board, [start[0], start[1] + (i * 1)], move_number):
            break
        else:
            if move_number % 2 == 0:
                rook_moves_w.append((start[0], start[1] + (i * 1)))
            else:
                rook_moves_b.append((start[0], start[1] + (i * 1)))
    for i in range(1, 8):
        if not validate_move(board, [start[0], start[1] + (i * -1)], move_number):
            break
        else:
            if move_number % 2 == 0:
                rook_moves_w.append((start[0], start[1] + (i * -1)))
            else:
                rook_moves_b.append((start[0], start[1] + (i * -1)))
    for i in range(1, 8):
        if not validate_move(board, [start[0] + (i * 1), start[1]], move_number):
            break
        else:
            if move_number % 2 == 0:
                rook_moves_w.append((start[0] + (i * 1), start[1]))
            else:
                rook_moves_b.append((start[0] + (i * 1), start[1]))
    for i in range(1, 8):
        if not validate_move(board, [start[0] + (i * -1), start[1]], move_number):
            break
        else:
            if move_number % 2 == 0:
                rook_moves_w.append((start[0] + (i * -1), start[1]))
            else:
                rook_moves_b.append((start[0] + (i * -1), start[1]))
    if move_number % 2 == 0:
        print("rooks starting is:", start)
        if check(board, move_number):
            new = filter_check(test_board, move_number, rook_moves_w, start)
            print("rook", new)
            return new
        final_list = filter_check(test_board, move_number, rook_moves_w, start)
        print("rook", final_list)
        return final_list
    else:
        if check(board, move_number):
            new = filter_check(test_board, move_number, rook_moves_b, start)
            # print("rook", new)
            return new
        final_list = filter_check(test_board, move_number, rook_moves_b, start)
        # print("rook", final_list)
        return final_list


def legal_queen_moves(board, start, move_number):
    rook_moves = legal_rook_moves(board, start, move_number)
    bishop_moves = legal_bishop_moves(board, start, move_number)
    queen_moves = rook_moves + bishop_moves
    # print("queen", queen_moves)
    return queen_moves


def legal_king_moves(board, move_number):
    test_board = board.copy()
    possible_moves = king_possibilities(board, move_number)
    legal_moves = []
    # Accounts for edges, but still has to be validated and make sure no checks
    for i in possible_moves:
        if validate_move(board, i, move_number) and controlled_squares(board, move_number, i):
            legal_moves.append(i)
    if check(board, move_number):
        new = filter_check(test_board, move_number, legal_moves, king_position(board, move_number))
        # print("king", new)
        return new
    final_list = filter_check(test_board, move_number, legal_moves, king_position(board, move_number))
    # print("king", final_list)
    return final_list


def filter_check(board, move_number, legal_moves, start):
    new_legal_moves = []
    for i in range(0, len(legal_moves)):
        initial_piece = find_piece(board, legal_moves[i])
        update_board(board, start, legal_moves[i])
        if not check(board, move_number):
            new_legal_moves.append(legal_moves[i])
            retract_move(board, start, legal_moves[i], initial_piece)
        else:
            retract_move(board, start, legal_moves[i], initial_piece)
    return new_legal_moves


def legal_en_passant(board, move_number, en_passant_square, start):
    enpassant_moves = []
    if en_passant_square != 0:
        if switch_player(move_number):
            if start[1] != en_passant_square[1] and start[0] + 1 == en_passant_square[0] and check_square(board,
                                                                                                          en_passant_square) == ".":
                enpassant_moves.append(en_passant_square)
        elif not switch_player(move_number):
            if start[1] != en_passant_square[1] and start[0] - 1 == en_passant_square[0] and check_square(board,
                                                                                                          en_passant_square) == ".":
                enpassant_moves.append(en_passant_square)
    # print("enpassant:", enpassant_moves)
    return enpassant_moves


def make_legal_move(move, board, start, end, move_number, en_passant_square, king_w, king_b, rook_w_l, rook_w_r,
                    rook_b_l,
                    rook_b_r, promotion_piece):
    """This function makes a move if it is legal"""
    # this function should have essentially what i had in main at first without making the move
    piece = find_piece(board, start)
    if move[0] == "O-O":
        castle(board, move[0], move_number, king_w, king_b, rook_w_l, rook_w_r, rook_b_l, rook_b_r)
    elif move[0] == "O-O-O":
        castle(board, move[0], move_number, king_w, king_b, rook_w_l, rook_w_r, rook_b_l, rook_b_r)
    else:
        if switch_player(move_number):  # for whites move
            if (65 <= ord(piece) <= 90) and (validate_move(board, end, move_number)):
                if piece == "P":
                    if pawn(board, start, end, move_number):
                        if end[0] == 8:
                            promotion(board, start, end, promotion_piece)
                        else:
                            update_board(board, start, end)
                    else:
                        if can_en_passant(board, en_passant_square, end, start, move_number):
                            execute_enpassant(board, start, end, move_number)
                elif piece == "K":
                    if king(start, end):
                        if controlled_squares(board, move_number, end):
                            update_board(board, start, end)
                elif piece == "N":
                    if knight(start, end):
                        update_board(board, start, end)
                elif piece == "B":
                    if bishop(board, start, end):
                        update_board(board, start, end)
                elif piece == "Q":
                    if queen(board, start, end):
                        update_board(board, start, end)
                elif piece == "R":
                    if rook(board, start, end):
                        update_board(board, start, end)
            else:
                return False
        if not switch_player(move_number):
            if (97 <= ord(piece) <= 122) and validate_move(board, end, move_number):
                if piece == "p":
                    if pawn(board, start, end, move_number):
                        if end[0] == 1:
                            promotion(board, start, end, promotion_piece)
                        else:
                            update_board(board, start, end)
                    else:
                        if can_en_passant(board, en_passant_square, end, start, move_number):
                            execute_enpassant(board, start, end, move_number)
                elif piece == "k":
                    if king(start, end):
                        if controlled_squares(board, move_number, end):
                            update_board(board, start, end)
                elif piece == "n":
                    if knight(start, end):
                        update_board(board, start, end)
                elif piece == "b":
                    if bishop(board, start, end):
                        update_board(board, start, end)
                elif piece == "q":
                    if queen(board, start, end):
                        update_board(board, start, end)
                elif piece == "r":
                    if rook(board, start, end):
                        update_board(board, start, end)
            else:
                return False
