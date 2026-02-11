# Gets the users weight inputted and error checks
userInput = input("Enter Weight of the item in Kg: ")
try:
    weight = float(userInput)
except ValueError:
    print("Enter as a number e.g 1.9, no need to put in kg or lb")
    input("Press any button to close!")
    exit()

# Base values, ground_shipping and drone_shipping are empty until calculated.
# The charges are set values not calculated
ground_shipping = 0
drone_shipping = 0
ground_charge = 20.00
premium_charge = 125.00

# Ground Shipping
if weight <= 2:
    ground_shipping = (1.50 * weight) + ground_charge
elif weight > 2 and weight <= 6:
    ground_shipping = (3.00 * weight) + ground_charge
elif weight > 6 and weight <= 10:
    ground_shipping = (4.00 * weight) + ground_charge
else:
    ground_shipping = (4.75 * weight) + ground_charge
print("Ground Shipping: $" + "%.2f" % ground_shipping)
print("Premium Ground shipping: $" + "%.2f" % premium_charge)

# Drone Shipping
if weight <= 2:
    drone_shipping = (4.50 * weight)
elif weight > 2 and weight <= 6:
    drone_shipping = (9.00 * weight)
elif weight > 6 and weight <= 10:
    drone_shipping = (12.00 * weight)
else:
    drone_shipping = (14.25 * weight)
print("Drone Shipping: $" + "%.2f" % drone_shipping)

# Cheapest, calculated the cheapest shipping option via min()
costList = [ground_shipping, drone_shipping, premium_charge]
print("Cheapest Shipping: $" + "%.2f" % min(costList))

input("Press any button to close!")


