import numpy as np

print("This program lets you play chess! enter the square you want to move your piece from to the square you want "
      "your piece to go to. Use standard chess notation. example: e2 e4, would be a move input. ")
board = [["R", "N", "B", "Q", "K", "B", "N", "R"], ["P", "P", "P", "P", "P", "P", "P", "P"],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."],
         ["p", "p", "p", "p", "p", "p", "p", "p"], ["r", "n", "b", "q", "k", "b", "n", "r"]]
while True:
    for i in range(len(board)):
        a = ' '.join(board[i])
        print(a)  # This is the board, created by joining each character in a list with a ' ', creating a new row in
        # every list of list
    move = input("Enter your move:").split()
    x = ord(move[0][1]) - 97  # Initial column number
    y = ord(move[1][1]) - 97  # Final column number
    piece = move[0][0]
    start = [int(move[0][2]), x]  # Row, column
    end = [int(move[1][1]), y]
    if board[int(move[0][2]) - 1][x] == ".":
        print("Your move isn't valid")


    def square_checker(dy, dx):
        if board[dx][dy] == ".":
            return True
        else:
            return False


    def rook(start, end):
        if x == y and abs(start[0] - end[0]) >= 0:
            for i in range(1, abs((start[0] - end[0]))):
                if board[x][i] != ".":
                    return False
                else:
                    return True
        elif x != y and start[0] == end[0]:
            for i in range(1, abs((x - y))):
                if board[i][start[0]] != ".":
                    return False
                else:
                    return True
        else:
            return False


    def knight(start, end):
        if x + 2 == y and (start[0] + 1) == end[0] or (start[0] - 1 == end[0]):
            return True
        elif x + 1 == y and start[0] + 2 == end[0] or (start[0] - 2 == end[0]):
            return True
        else:
            return False


    def king(start, end):
        if x + 1 == y or x - 1 == y and (start[0] + 1 == end[0] or start[0] - 1 == end[0]):
            return True
        else:
            return False


    def pawn(start, end):
        for i in range(1):
            if board[i][x] != ".":
                return False
        if start[0] == 2 and x == y:
            if start[0] + 2 == end[0] or (start[0] + 1 == end[0]):
                return True
        elif start[0] != 2 and x == y:
            if start[0] + 1 == end[0]:
                return True
        elif start[0] != 8 and x != y:
            if (x + 1 == y or x - 1 == y) and start[0] + 1 == end[0]:
                return True


    def bishop(start, end):
        x_dir = np.sign(y - x)  # Direction of letters
        y_dir = np.sign(end[0] - start[0])  # Direction of numbers
        if abs(y - x) != abs(end[0] - start[0]):
            return False
        elif abs(y - x) != abs(end[0] - start[0]):
            for i in range(1, abs(y - x)):
                if square_checker(start[0] + (i * y_dir), start[1] + (i * x_dir)):
                    return True


    def queen():
        if rook(start, end) and bishop(start, end):
            return True
        else:
            return False