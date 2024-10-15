from string import ascii_lowercase as abc


class Board:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.board_dictionary = self.generate()

    def generate(self):                                              # Creates the Dict to store the board data
        count = 1                                                    # used to get 1, 2, 3
        abc_count = 0                                                # used to get a, b, c
        board_dictionary = {}
        for x in range(0, self.y_size):
            for i in range(0, self.x_size):
                board_dictionary[abc[abc_count] + str(count)] = " "  # abc[0] + 1 == a1
                count += 1
            count = 1                                                # resets counter to rows so goes no higher than 3
            abc_count += 1                                           # progresses to the next letter
        return board_dictionary

    def display(self):                                              # Displays the Board GUI to the terminal
        row_list = []
        for key in self.board_dictionary.keys():                    # places the Dict values in a list
            row_list.append(self.board_dictionary.get(key))

        print(" +---+---+---+")
        print(f"C| {row_list[6]} | {row_list[7]} | {row_list[8]} |")
        print(" |---+---+---|")
        print(f"B| {row_list[3]} | {row_list[4]} | {row_list[5]} |")
        print(" |---+---+---|")
        print(f"A| {row_list[0]} | {row_list[1]} | {row_list[2]} |")
        print(" +---+---+---+")
        print("   1   2   3  ")


class Player:
    player_count = 0

    def __init__(self, name="VOID"):
        self.name = name
        Player.player_count += 1
        self.player_number = Player.player_count
        self.player_piece = self.get_piece()

    @staticmethod
    def get_piece():
        if Player.player_count == 1:
            return "X"
        elif Player.player_count == 2:
            return "O"

    @staticmethod
    def choice():
        choice = input("Where would you like to place your piece?\n-")
        return choice


class Game:
    def __init__(self, x_size=3, y_size=3):
        self.player1 = Player()
        self.player2 = Player()
        self.board = Board(x_size, y_size)
        self.menu()

    @staticmethod
    def menu():
        print("         Welcome to      \n"
              "    NOUGHTS AND CROSSES! \n"
              "                         \n")
        input("   Press any key to start!")

    def valid_placement(self, choice, piece):
        for key in self.board.board_dictionary.keys():
            if choice not in self.board.board_dictionary.keys():
                print("That is not a valid placement!\n")
                return False
            elif self.board.board_dictionary.get(key) != " ":
                print("That is not a valid placement!\n")
                return False
            elif choice == key:
                self.board.board_dictionary[choice] = piece
            return True


game = Game(3, 3)
game.board.display()
while True:
    while True:
        print("Player 1's Turn!")
        game.valid_placement(game.player1.choice(), game.player1.player_piece)
        game.board.display()
        break
    while True:
        print("Player 2's Turn!")
        game.valid_placement(game.player2.choice(), game.player2.player_piece)
        game.board.display()
        break




