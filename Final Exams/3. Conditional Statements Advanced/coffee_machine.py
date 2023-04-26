drink_type = input()
sugar = input()
number_of_drinks = int(input())

price = None

if drink_type == "Espresso":
    if sugar == "Without":
        price = 0.9 * 0.65
        if number_of_drinks >= 5:
            price *= 0.75
    elif sugar == "Normal":
        price = 1
        if number_of_drinks >= 5:
            price *= 0.75
    else:
        price = 1.2
        if number_of_drinks >= 5:
            price *= 0.75
elif drink_type == "Cappuccino":
    if sugar == "Without":
        price = 0.65
    elif sugar == "Normal":
        price = 1.2
    else:
        price = 1.6
else:
    if sugar == "Without":
        price = 0.5 * 0.65
    elif sugar == "Normal":
        price = 0.6
    else:
        price = 0.7

total_sum = number_of_drinks * price

if total_sum > 15:
    total_sum *= 0.8

print(f"You bought {number_of_drinks} cups of {drink_type} for {total_sum:.2f} lv.")