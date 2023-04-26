number = int(input())
type_of_glass = input()
delivery_method = input()

price = 0

if type_of_glass == "90X130":
    price = 110
    if number > 60:
        price = 110 * 0.92
    elif number > 30:
        price = 110 * 0.95
elif type_of_glass == "100X150":
    price = 140
    if number > 80:
        price = 140 * 0.9
    elif number > 40:
        price = 140 * 0.94
elif type_of_glass == "130X180":
    price = 190
    if number > 50:
        price = 190 * 0.88
    elif number > 20:
        price = 190 * 0.93
elif type_of_glass == "200X300":
    price = 250
    if number > 50:
        price = 250 * 0.86
    elif number > 25:
        price = 250 * 0.91

price = price * number

if delivery_method == "With delivery":
    price = price + 60
else:
    price = price

if number > 99:
    price *= 0.96

if number < 10:
    print("Invalid order")
else:
    print(f"{price:.2f} BGN")