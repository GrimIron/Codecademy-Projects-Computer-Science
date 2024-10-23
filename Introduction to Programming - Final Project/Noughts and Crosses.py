from string import ascii_lowercase as abc


class Board:
    def __init__(self, x_size, y_size):
        self.x_size = x_size                                           # Sets the Y axis size of Board
        self.y_size = y_size                                           # Sets the X axis size of Board
        self.board_dictionary = self.generate()                        # Creates Dict for the board using the x/y size

    def generate(self):                                                # Creates the Dict to store the board data
        count = 1                                                      # used to get 1, 2, 3
        abc_count = 0                                                  # used to get a, b, c
        board_dictionary = {}
        for x in range(0, self.y_size):
            for i in range(0, self.x_size):
                board_dictionary[abc[abc_count] + str(count)] = " "    # abc[0] + 1 == a1
                count += 1
            count = 1                                                  # resets count so no higher than 3
            abc_count += 1                                             # progresses to the next letter
        return board_dictionary

    def display(self):                                                 # Displays the Board GUI to the terminal
        row_list = []
        for key in self.board_dictionary.keys():                       # places the Dict values in a list
            row_list.append(self.board_dictionary.get(key))
        print(" +---+---+---+")
        print(f"C| {row_list[6]} | {row_list[7]} | {row_list[8]} |")
        print(" |---+---+---|")
        print(f"B| {row_list[3]} | {row_list[4]} | {row_list[5]} |")
        print(" |---+---+---|")
        print(f"A| {row_list[0]} | {row_list[1]} | {row_list[2]} |")
        print(" +---+---+---+")
        print("   1   2   3  ")


class Player:                                                          # Keeps functions/ values for the player
    player_count = 0                                                   # Keeps track of number of players

    def __init__(self, name="VOID"):                                   # Creates the player
        self.name = name                                               # Gets the players name
        Player.player_count += 1                                       # +1 for every player
        self.player_number = Player.player_count                       # Gets player number based on order created
        self.player_piece = self.get_piece()                           # Uses get_piece to get GUI Piece

    @staticmethod
    def get_piece():                                                   # Gets the players GUI Piece based on number
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

    def valid_placement(self, choice, piece):                           # Checks if piece placement is a valid location
        # print(choice)
        for key in self.board.board_dictionary.keys():
            # print(key)
            if choice not in self.board.board_dictionary.keys():
                print("That is not a valid placement!\n")
                return True
            elif self.board.board_dictionary.get(choice) != " ":
                # print("-" + self.board.board_dictionary.get(key))
                print("Theres already a piece there!!!\n")
                return True
            elif choice == key:
                self.board.board_dictionary[choice] = piece
                #print(self.board.board_dictionary)
                return False

    @staticmethod
    def check_victory():                                                # Check if player has met victory condition
        victory = [["c1", "c2", "c3"], ["a1", "a2", "a3"], ["b1", "b2", "b3"],
                   ["c1", "b1", "a1"], ["c2", "b2", "a2"], ["c3", "b3", "a3"],
                   ["c1", "b2", "a3"], ["c3", "b2", "a1"]]
        x_count = 0
        o_count = 0
        winner = ""
        for victory_sub_list in victory:
            for value in victory_sub_list:
                if game.board.board_dictionary.get(value) == "X":
                    x_count += 1
                elif game.board.board_dictionary.get(value) == "O":
                    o_count += 1
            if x_count == 3:
                winner = "X"
                return True, winner
            elif o_count == 3:
                winner = "O"
                return True, winner
            else:
                x_count = 0
                o_count = 0
        return False

    def game_over(self):
        count = 0
        # print("Count1: " + str(count))
        for key in game.board.board_dictionary:
            # print("Key: " + str(key))
            # print(game.board.board_dictionary.get(key))
            if game.board.board_dictionary.get(key) != " ":
                count += 1
        if count == self.board.y_size * self.board.x_size:
            return False
        elif self.check_victory():
            winner = self.check_victory()
            if winner[1] == "X":
                print("The Winner is Player 1!")
            elif winner[2] == "O":
                print("The Winner is Player 2!")
            else:
                print("Error! I need an Adult!")
            return False
        else:
            # print("Count2: " + str(count))
            return True


game = Game(3, 3)
game.board.display()
while game.game_over():
    print("Player 1's Turn!")
    while game.valid_placement(game.player1.choice(), game.player1.player_piece):

        game.board.display()
    game.board.display()
    if not game.game_over():
        break
    print("Player 2's Turn!")
    while game.valid_placement(game.player2.choice(), game.player2.player_piece):
        game.board.display()
    game.board.display()



