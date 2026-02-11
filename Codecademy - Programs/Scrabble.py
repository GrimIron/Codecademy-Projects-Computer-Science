letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
letters = [letter.upper() for letter in letters]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Combines letters and points into a dictionary of Keys(letters), values(points) and adds another key/value to the
# dict for a Space.
letter_to_points = dict(zip(letters, points))
letter_to_points[" "] = 0


# Takes a word as an argument, formats it to uppercase and uses the Dict to get a point total for the word.
def score_word(word):
    uppercase_word = word.upper()
    point_total = 0
    for letter in uppercase_word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


# A test list to make sure the above code works
# brownie_points = score_word("BROWNIE")
# print("The score for BROWNIES is: " + str(brownie_points))


# A Dict and players and there words
player_to_words = {"player1": ["Blue", "Tennis", "Exit"],
                   "wordNerd": ["Earth", "Eyes", "Machine"],
                   "Lexi Con": ["Eraser", "Belly", "Husky"],
                   "Prof Reader": ["Zap", "Coma", "Period"]}


# Adds a word to the words a player as played, and returns an error if the player is not found
def play_word(player, word):
    try:
        dictionary = player_to_words.get(player)
        dictionary.append(word)
    except:
        print("Player Not Found!")


# Gets the list of words for each player and adds the score of these words together and adds the player and score to a
# new Dict and returns
def update_point_totals(dictionary):
    player_to_points = {}
    # Gets players name
    for player in player_to_words:
        player_points = 0
        # Uses name to get their word list
        words = player_to_words.get(player)
        # Iterates through the list of words and runs score_word() to get the word score and appends the the players overall score
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    # Returns Dict player_to_points
    return player_to_points


player_to_points = update_point_totals(player_to_words)

# Sorts the Dictionary by the values from highest to lowest
players_sorted = dict(sorted(player_to_points.items(), key=lambda x: x[1], reverse=True))

# Displays the player scores, to the terminal
for player, score in players_sorted.items():
    print(f"{player} Score: {score}")




