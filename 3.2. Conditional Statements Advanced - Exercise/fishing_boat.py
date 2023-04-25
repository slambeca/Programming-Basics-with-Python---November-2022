budget = int(input())
season = input()
count_fishermen = int(input())

rent_price = 0

if season == "Spring":
    rent_price = 3000
elif season == "Summer":
    rent_price = 4200
elif season == "Autumn":
    rent_price = 4200
elif season == "Winter":
    rent_price = 2600

if count_fishermen <= 6:
    rent_price *= 0.9
elif count_fishermen <= 11:
    rent_price *= 0.85
elif count_fishermen >= 12:
    rent_price *= 0.75

if count_fishermen % 2 == 0 and season != "Autumn":
    rent_price *= 0.95

if budget >= rent_price:
    print(f"Yes! You have {budget - rent_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - rent_price):.2f} leva.")