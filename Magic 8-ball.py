import random

# Base values
name = input("What is your name? \n")
question = input("What is your question? \n")
answer = ""
random_number = random.randint(1, 10)

# Checks if the user had inputted a name
if name == "":
    print("Question: " + question)
else:
    print(name + " asks: " + question + "?")

# Checks if the user has inputted a question
if question == "":
    print("Theres no question! Help! HELP!")
    exit()
else:
    print("Magic 8-Ball's answer: ", end="")

# Checks the random_number for the 8-ball response
if random_number == 1:
    print("Yes - definitely")
elif random_number == 2:
    print("It is decidedly so")
elif random_number == 3:
    print("Without a doubt")
elif random_number == 4:
    print("Reply hazy, try again")
elif random_number == 5:
    print("Ask again later")
elif random_number == 6:
    print("Better not tell you now")
elif random_number == 7:
    print("My sources say no")
elif random_number == 8:
    print("Outlook not so good")
elif random_number == 9:
    print("Very doubtful")
elif random_number == 10:
    print("If the gods will it")
else:
    print("error out of range")

input("Press any button to close!")
