import random


class Words:
    def __init__(self):
        self.word_choice = self.get_word()
        self.letters = self.get_letters()
        self.word_length = self.get_word_length()

    def return_data(self):
        return self.word_choice, self.letters, self.word_length

    # Selects a word from a list of possible words and formats to lower case
    def get_word(self):
        word_file = open("list of possible words", "r")
        list_of_words = []
        for word in word_file:
            list_of_words.append(word)
        self.word_choice = list_of_words[random.randint(0, len(list_of_words) - 1)].upper().strip("\n")
        return list(self.word_choice)

    # Breaks word down into a list of letters
    def get_letters(self):
        letter_list = []
        for letter in self.word_choice:
            letter_list.append(letter)
        return letter_list

    # Gets the length on the word as a int
    def get_word_length(self):
        word_length = len(self.word_choice)
        return word_length

    # Checks to see if the letter appears in the word
    def check_letter(self):
        for letter in self.letters:
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
