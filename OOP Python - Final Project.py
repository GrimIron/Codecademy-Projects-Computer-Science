
# OLD CODE NO USE














































"""
class Piece:
    def __init__(self, position, type):
        self.position = position
        self.type = type


class Board:
    def __init__(self, size):
        self.size = size
        self.board = []

    def generate_board(self):
        count = 0
        # creates and populates the board
        for y in range(self.size):
            row = []
            for x in range(self.size):
                row.append(str(count))
                count += 1
            self.board.append(row)
        return self.board

    def display_board(self):
        print("    A   B   C   D   E   F   G   H")
        print("  +---+---+---+---+---+---+---+---+")
        count = 1
        # Displays the number on the Y Axis of the board
        for y in range(8):
            print(str(count), end=" |")
            # displays the contents of the board
            for x in range(8):
                print(" " + str(board[y][x]), end=" |")
            print("")
            print("  +---+---+---+---+---+---+---+---+")
            count += 1


class Player:
    pass


chess_board = Board(8)
board = chess_board.generate_board()
chess_board.display_board()





# first iteration of printing a board
print("    A   B   C   D   E   F   G   H")
print("  +---+---+---+---+---+---+---+---+")
count = 1
for x in range(8):
    print(str(count), end=" ")
    for y in range(8):
        print(board[x][y], end="")

    print("|")
    print("  +---+---+---+---+---+---+---+---+")
    count += 1"""


