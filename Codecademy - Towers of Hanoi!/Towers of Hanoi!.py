from Stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Creates the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Gets the number of discs to play
num_discs = int(input("\nHow many disks do you want to play with?\n"))
while num_discs < 3:
  num_discs = int(input("Enter a number greater than or equal to 3\n"))

#Pushes the discs on to the left tower
for i in range(num_discs, 0, -1):
  left_stack.push(i)

#Calculates optimal moves
num_optimal_moves = 2**num_discs - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

#Get User Input, formats to upper case and checks if a valid choice. Allows users to enter the first letter of the tower to choose it. eg. L = Left M = Middle R = Right
def get_input():
  choices = [stack.get_name()[0] for stack in stacks] # L, M, R
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f"Enter {letter} for {name}")
    user_input = input("")
    if user_input.upper() in choices:
      for i in range(len(stacks)):
        if user_input.upper() == choices[i]:
          return stacks[i]

#Sets up the core game loop and tracks user moves
num_user_moves = 0
while (right_stack.get_size()) != num_discs:
  print("\n\n\n...Current Stacks...")
  for i in stacks:
    i.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. That Tower is Empty! Try Again")
    elif (to_stack.is_empty()) or (from_stack.peek() < to_stack.peek()):
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
  print(f"\n\nYou Completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")




