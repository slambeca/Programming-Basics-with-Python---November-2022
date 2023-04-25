type_flower = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if type_flower == "Roses":
    if number_of_flowers > 80:
        price = 5 * 0.9
    else:
        price = 5
elif type_flower == "Dahlias":
    if number_of_flowers > 90:
        price = 3.8 * 0.85
    else:
        price = 3.8
elif type_flower == "Tulips":
    if number_of_flowers > 80:
        price = 2.8 * 0.85
    else:
        price = 2.8
elif type_flower == "Narcissus":
    if number_of_flowers < 120:
        price = 3 * 1.15
    else:
        price = 3
else:
    if number_of_flowers < 80:
        price = 2.5 * 1.2
    else:
        price = 2.5

total_price = number_of_flowers * price

if total_price <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flower} and {budget - total_price:.2f} "
          f"leva left.")
elif total_price > budget:
    print(f"Not enough money, you need {abs(budget - total_price):.2f} leva more.")