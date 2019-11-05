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


    def rook(start, end, move):
        if x == y and abs(start[0] - end[0]) >= 0:
            for i in range(1, abs((start[0] - end[0]))):
                if board[x][i] != ".":
                    return False
                else:
                    return True
        elif x != y and move[0][2] == move[1][2]:
            for i in range(1, abs((x - y))):
                if board[i][start[0]] != ".":
                    return False
                else:
                    return True
        else:
            return False


    def knight(start, end, move):
        if x + 2 == y and (int(move[0][2]) + 1 == int(move[1][2]) or (int(move[0][2]) - 1 == int(move[1][2]))):
            return True
        elif x + 1 == y and (int(move[0][2]) + 2 == int(move[1][2]) or int(move[0][2]) - 2 == int(move[1][2])):
            return True
        else:
            return False


    def king(start, end, move):
        if x + 1 == y or x - 1 == y and (int(move[0][2]) + 1 == move[1][2] or int(move[0][2]) - 1 == move[1][2]):
            return True
        else:
            return False


    def pawn(start, end, move):
        for i in range(1):
            if board[i][x] != ".":
                return False
        if move[0][2] == 2 and x == y:
            if (int(move[0][2]) + 2 == int(move[1][2])) or (int(move[0][2]) + 1 == int(move[1][2])):
                return True
        elif int(move[0][2]) != 2 and x == y:
            if int(move[0][2]) + 1 == int(move[1][2]):
                return True
        elif int(move[0][2]) != 8 and x != y:
            if (x + 1 == y or x - 1 == y) and int(move[0][2]) + 1 == int(move[1][2]):
                return True


    def bishop(start, end, move):
        x_dir = np.sign(y - x)  # Direction of letters
        y_dir = np.sign(end[0] - start[0])  # Direction of numbers
        if abs(y - x) != abs(end[0] - start[0]):
            return False
        elif abs(y - x) != abs(end[0] - start[0]):
            for i in range(1, abs(y - x)):
                if square_checker(start[0] + (i * y_dir), start[1] + (i * x_dir)):
                    return True


    def queen():
        if rook(start, end, move) and bishop(start, end, move):
            return True
        else:
            return False


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
    x = ord(move[0][1]) - 97
    y = ord(move[1][1]) - 97
    piece = move[0][0]
    start = [int(move[0][2]), x]
    end = [int(move[1][1]), y]
    if board[int(move[0][2]) - 1][x] == ".":
        print("Your move isn't valid")
    if move[0][0] == "N" or move[0][0] == "n":
        if x + 2 == y and (int(move[0][2]) + 1 == int(move[1][2]) or (int(move[0][2]) - 1 == int(move[1][2]))):
            board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
            board[int(move[0][2]) - 1][x] = "."
        elif x + 1 == y and (int(move[0][2]) + 2 == int(move[1][2]) or int(move[0][2]) - 2 == int(move[1][2])):
            board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
            board[int(move[0][2]) - 1][x] = "."
        else:
            print("Your move isn't valid")


    def rook(start, end, move):
        if move[0][0] == "R" or move[0][0] == "r":
            if x == y and abs(start[0] - end[0]) >= 0:
                for i in range(1, abs((start[0] - end[0]))):
                    if board[x][i] != ".":
                        print("That move isn't valid")
                    else:
                        board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
                        board[int(move[0][2]) - 1][x] = "."
            elif x != y and move[0][2] == move[1][2]:
                for i in range(1, abs((x - y))):
                    if board[i][start[0]] != ".":
                        print("Your move is invalid")
                    else:
                        board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
                        board[int(move[0][2]) - 1][x] = "."
            else:
                print("Your move isn't valid")


    if move[0][0] == "K" or move[0][0] == "k":
        if x + 1 == y or x - 1 == y and (int(move[0][2]) + 1 == move[1][2] or int(move[0][2]) - 1 == move[1][2]):
            board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
            board[int(move[0][2]) - 1][x] = "."
        else:
            print("your move isn't valid")
    if move[0][0] == "P" or move[0][0] == "p":
        for i in range(1):
            if board[i][x] != ".":
                print("your move is invalid")
        if move[0][2] == 2 and x == y:
            if (int(move[0][2]) + 2 == int(move[1][2])) or (int(move[0][2]) + 1 == int(move[1][2])):
                board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
                board[int(move[0][2]) - 1][x] = "."
        elif int(move[0][2]) != 2 and x == y:
            if int(move[0][2]) + 1 == int(move[1][2]):
                board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
                board[int(move[0][2]) - 1][x] = "."
        elif int(move[0][2]) != 8 and x != y:
            if (x + 1 == y or x - 1 == y) and int(move[0][2]) + 1 == int(move[1][2]):
                board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
                board[int(move[0][2]) - 1][x] = "."


    def bishop(start, end, move):
        if x - y > 0 and (start[0] - end[0] < 0):  # To the left and up
            for i in range(1, abs(start[0] - end[0])):
                if board[start[0] + i][start[1] + i] != ".":
                    print("Your move is invalid")
                elif board[start[0] - i][start[1] + i] != ".":
                    print("Your move is invalid")
                elif board[start[0] + i][start[1] - i] != ".":
                    print("Your move is invalid")
                elif board[start[0] - i][start[1] - i] != ".":
                    print("Your move is invalid")
                elif abs(x - y) == abs(start[0] - end[0]):
                    board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
                    board[int(move[0][2]) - 1][x] = "."
            else:
                print("your move isn't valid")


    if move[0][0] == "Q" or move[0][0] == "q":
        if abs(x - y) == abs(int(move[0][2]) - int(move[1][2])):
            board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
            board[int(move[0][2]) - 1][x] = "."
        elif x == y and abs(int(move[0][2]) - int(move[1][2])) >= 0:
            board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
            board[int(move[0][2]) - 1][x] = "."
        elif x != y and move[0][2] == move[1][2]:
            board[int(move[1][2]) - 1][y] = board[int(move[0][2]) - 1][x]
            board[int(move[0][2]) - 1][x] = "."
        else:
            print("your move isn't valid")
