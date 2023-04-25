budget = float(input())
category = input()
number_of_people = int(input())

transport = None
price = None

if category == "VIP":
    price = 499.99
else:
    price = 249.99

if 1 <= number_of_people <= 4:
    transport = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport = budget * 0.6
elif 10 <= number_of_people <= 24:
    transport = budget / 2
elif 25 <= number_of_people <= 49:
    transport = budget * 0.4
else:
    transport = budget / 4

diff = abs(budget - transport)

price = price * number_of_people

if diff >= price:
    print(f"Yes! You have {abs(diff - price):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff - price):.2f} leva.")