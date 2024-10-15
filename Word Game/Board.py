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