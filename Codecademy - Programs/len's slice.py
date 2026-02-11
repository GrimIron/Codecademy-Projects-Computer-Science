# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

pizza_and_prices = []
count = 0
for i in toppings:
    pizza_and_prices.append([prices[count], toppings[count]])
    count = count + 1

#sorts in asending order
pizza_and_prices.sort()

#gets the number of $2 slices
num_two_dollar_slices = prices.count(2)

#gets the number of pizzas
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!\n")

#displays the cost and types of pizza
for i in pizza_and_prices:
    print("$" + str(i[0]) + " " + str(i[1]))

#displays the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print("\nThe cheapest pizza is: " + str(cheapest_pizza[1]) + " at $" + str(cheapest_pizza[0]) )

#displays the priciest pizza
priciest_pizza = pizza_and_prices[-1]
print("\nThe most expensive pizza is: " + str(priciest_pizza[1]) + " at $" + str(priciest_pizza[0]))

#removes the most expensive pizza adds a new topping option
pizza_and_prices.pop()
pizza_and_prices.insert(4, [2.5, "peppers"])

#gets the three cheapest pizzas and displays them
three_cheapest = pizza_and_prices[:3]
print("\nThe three cheapest pizzas are: ")
for i in three_cheapest:
    print("$" + str(i[0]) + " " + str(i[1]))

print(pizza_and_prices)
