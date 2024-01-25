print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
print("You are on: ", end="")

weight = 185
planet = 3
gravity = 1

# Write an if statement below:
if planet == 1:
    print("Venus")
    gravity = 0.91
elif planet == 2:
    print("Mars")
    gravity = 0.38
elif planet == 3:
    print("Jupiter")
    gravity = 2.34
elif planet == 4:
    print("Saturn")
    gravity = 1.06
elif planet == 5:
    print("Uranus")
    gravity = 0.92
else:
    print("Neptune")
    gravity = 1.19

# Calculates weight on the destination planet
destinationWeight = 185 * gravity
print("Your weight is: " + str(destinationWeight))
