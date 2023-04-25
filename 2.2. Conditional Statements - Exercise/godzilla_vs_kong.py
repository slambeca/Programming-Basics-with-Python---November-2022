budget = float(input())
statists = int(input())
price_clothes_statist = float(input())

decor_cost = budget * 0.1
price_for_clothing = statists * price_clothes_statist

if statists > 150:
    price_for_clothing = price_for_clothing * 0.9

total = decor_cost + price_for_clothing

if total <= budget:
    print(f"Action! \nWingard starts filming with {budget - total:.2f} leva left.")
elif total > budget:
    print(f"Not enough money! \nWingard needs {total - budget:.2f} leva more.")