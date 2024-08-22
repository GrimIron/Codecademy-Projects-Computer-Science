import random


class Words:
    def __init__(self):
        self.list_of_words = []
        self.word_choice = "Use get_word() to Generate a word!"

    # Selects a word from a list of possible words and formats to lower case
    def get_word(self):
        word_file = open("list of possible words", "r")
        for word in word_file:
            self.list_of_words.append(word)
        self.word_choice = self.list_of_words[random.randint(0, len(self.list_of_words) - 1)].upper().strip("\n")
        return list(self.word_choice)

    # Gets the length on the word as a int
    def get_word_length(self):
        word_length = len(self.word_choice)
        return word_length

    # Checks to see if the letter appears in the word
    def check_letter(self, letter_list):
        for letter in letter_list:
            if letter in self.word_choice:
                return True
            else:
                return False

    # Gets the index positions where the letter appears in the word
    def get_letter_position(self, letter):
        letter_index = []
        count = 0
        for x in self.word_choice:
            if x == letter:
                letter_index.append(count)
            else:
                pass
            count += 1
        return letter_index


class Board:
    def __init__(self):
        self.row = []

    # Creates the list used to display the word
    def generate_empty_board(self, word):
        counter = 0
        for letter in word:
            self.row.append(letter)
            counter += 1

    # Displays the board to the terminal
    def display_board(self, chosen_word, player_letters):
        count = 0
        # e.g: +---+---+---+---+---+
        for i in chosen_word:
            print("+---", end="")
        print("+")
        try:
            # e.g: |    |    |    |    |
            for letter in self.row:
                if letter == player_letters[count]:
                    print(f"| {str(letter)}", end=" ")
                    count += 1
                else:
                    print(f"|   ", end="")
                    count += 1
        except IndexError:
            # e.g: |    |    |    |    |
            for letter in self.row:
                print(f"|   ", end="")
        print("|")
        # e.g: +---+---+---+---+---+
        for i in chosen_word:
            print("+---", end="")
        print("+")


class Game:
    def __init__(self):
        self.difficulty = 0                                 # The number of mistakes a user can make
        self.player_letter_choice = []                      # Saves the users letter input for use
        self.words = Words()                                # Initialises the Words class
        self.chosen_word = self.words.get_word()            # Gets a word from the list of possible words
        self.board = Board()                                # Initialises the Board class, word length to set its scale
        self.board.generate_empty_board(self.chosen_word)   # Generates the board info
        self.board.display_board(self.chosen_word,          # Displays an EMPTY board the size of the word to the player
                                 self.player_letter_choice)
        self.player_mistakes = 0                            # Count for how many guesses the player has made
        self.working_list = self.create_working_list()      # Creates a empty list the length of the chosen word

    # Gets players input and checks formating/ error checks
    def player_input(self):
        while True:
            player_input = str(input("Please enter a letter: ")).upper()
            if player_input.isalpha() != True:
                print("Do not enter a number... they are not letters")
                continue
            elif len(player_input) > 1:
                print("Please enter ONE letter!")
                continue
            elif player_input in self.player_letter_choice:
                print("You have already used that letter! Try Another!")
                continue
            else:
                self.player_letter_choice.append(player_input)
                break

    # Creates an empty list the size of the word, where the players correct letter guesses get placed
    def create_working_list(self):
        temp = []
        for i in range(0, int(len(self.chosen_word))):
            temp.append(" ")
        return temp

    # Displays letters on UI
    def place_letters(self):
        last_letter = self.player_letter_choice[-1]                         # Gets the last letter played by the user
        if self.words.check_letter(last_letter):                            # Checks if letter is in word
            print(f"{last_letter} is in the word!")
            letter_position = self.words.get_letter_position(last_letter)   # Gets the index position of the letter
            for index in letter_position:                                   # Adds the letter to the indexes in the list
                self.working_list[index] = last_letter
            self.board.display_board(self.chosen_word, self.working_list)
        else:
            print(f"{last_letter} is not in the word!")
            self.player_mistakes += 1

    # Displays the list of letters the user had inputted
    def display_played_letters(self):
        print(f"You have used the letters: ", end="")
        for i in self.player_letter_choice:
            print(f"{i}, ", end="")
        print()

    # Plays the game
    def play_round(self):
        self.board.display_board(self.chosen_word, self.player_letter_choice)
        while True:
            self.player_input()                         # Gets the player input and appends to self.player_letter_choice
            self.place_letters()                        # Places the letter the user chooses into self.working_list
            self.display_played_letters()               # displays the board with the correct letters to the terminal
            # Checks in the user is below the max number of mistakes
            if self.player_mistakes > self.difficulty:
                print("GAME OVER!")
                input("")
                return False
            elif self.working_list == self.chosen_word:
                print("YOU WON!")
                input("")
                return False

    # Displays a start screen to the user
    def ui(self):
        print("Welcome to TBA\n"
              "What difficulty do you want to choose?\n"
              "[1] Very Easy (10 Guesses)\n"
              "[2]   Easy    (8 Guesses)\n"
              "[3]  Normal   (6 Guesses)\n"
              "[4]   Hard    (4 Guesses)\n"
              "[5] Very Hard (2 Guesses)\n")

        # Asks the user to choose a difficulty level, then sets how many mistakes they can make
        while True:
            try:
                choice = int(input("Please enter a Number:"))
                break
            except ValueError:
                print("Enter a Number!!!")
        if choice == 1:
            self.difficulty = 10
        elif choice == 2:
            self.difficulty = 8
        elif choice == 3:
            self.difficulty = 6
        elif choice == 4:
            self.difficulty = 4
        else:
            self.difficulty = 2

        self.play_round()       # runs a round of the game

        # Checks to see if the user wants to play again
        while True:
            try:
                choice = str(input("Would you like to play again?: \n"
                                   "[Y] Yes \n"
                                   "[N] NO \n")).upper()
                print(choice)
                if choice == "Y" or choice == "N":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Enter Y or N")
        if choice == "Y":
            new_game = Game()   # Creates a new instance of the game
            new_game.ui()
        else:
            print("Thanks for playing!")


game = Game()
game.ui()