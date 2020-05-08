from board import *
from player import *
from pieces import *
from checks import *
from legal_moves import *

# TODO: cannot capture own pieces(add function to main), add castle to legal moves,
#  maybe implement a function that finally gives if a move is legal to simplify main
move_number = 0
board = create_new()
rook_b_l = 0
rook_w_r = 0
rook_b_r = 0
rook_w_l = 0
king_w = 0
king_b = 0
en_passant_square = 0
history = []
promotion_piece = 0
checking_pieces = 0

while True:  # change this to while not checkmate later
    # move_number is auto added 1 whenever update_board() is called
    move = str(input("Enter your move:")).split()
    if move[0] == "a1":
        rook_w_l += 1
    elif move[0] == "h1":
        rook_w_r += 1
    elif move[0] == "e1":
        king_w += 1
    elif move[0] == "e8":
        king_b += 1
    elif move[0] == "a8":
        rook_b_r += 1
    elif move[0] == "h8":
        rook_b_l += 1
    column = ord(move[0][0]) - 97
    fin_column = ord(move[1][0]) - 97
    start = [int(move[0][1]), column]  # Row, column
    end = [int(move[1][1]), fin_column]
    history.append(start)
    history.append(end)
    print("start", start)
    print("end", end)
    piece = find_piece(board, start)
    piece_end = find_piece(board, end)

    if end[0] == 8 and (piece == "P" or piece == "p"):
        promotion_piece = move[1][3]
    elif end[0] == 1 and (piece == "P" or piece == "p"):
        promotion_piece = move[1][3]
    if piece != "P":
        en_passant_square = 0
    if piece == "P":
        if start[0] + 2 == end[0]:
            en_passant_square = [end[0] - 1, end[1]]
        else:
            en_passant_square = 0
    if piece != "p":
        en_passant_square = 0
    if piece == "p":
        if start[0] - 2 == end[0]:
            en_passant_square = [end[0] + 1, end[1]]
        else:
            en_passant_square = 0
    make_legal_move(move, board, start, end, move_number, en_passant_square, king_w, king_b, rook_w_l, rook_w_r,
                    rook_b_l, rook_b_r, promotion_piece)
    show_board(board)
    move_number += 1
    print(all_legal_moves(board, move_number, en_passant_square))
    if check(board, move_number):
        # print(move_number)
        #checking_pieces = pieces_controlled_squares(board, move_number)
        print("Check!")
        #if checkmate(board, move_number, checking_pieces):
         #   print("Checkmate!")
        #else:
         #   checking_pieces = 0
    #if stalemate(all_legal_moves(board, move_number, en_passant_square)):
        #print("Stalemate!")
        #exit()

# when its check your move must be in king poss or the square of checking piece and it should not be check still
