hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# calculates average price of a cut
total_price = 0
for number in prices:
    total_price += number
average_price = total_price / len(prices)
print(f"Average Haircut Price: £{average_price}")

new_prices = [number - 5 for number in prices]

# calculates total revenue
total_revenue = 0
for i in range(0, len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print(f"Total Revenue: £{total_revenue}")

# calculates daily average revenue
average_daily_revenue = total_revenue / 7
print(f"Total Daily Revenue: £{average_daily_revenue}")

# creates a list of haircuts under 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print("Haircuts under £30: ", end="")
for i in range(len(cuts_under_30)):
    print(cuts_under_30[i], end=", ")

input("Press any button to close!")

