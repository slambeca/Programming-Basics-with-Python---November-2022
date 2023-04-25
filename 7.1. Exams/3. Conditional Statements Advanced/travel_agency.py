city = input()
package = input()
vip = input()
days = int(input())
cities = ("Bansko", "Borovets", "Varna", "Burgas")
packages = ("noEquipment", "withEquipment", "noBreakfast", "withBreakfast")

price = 0

if days > 7:
    days -= 1

if city not in cities or package not in packages:
    print("Invalid input!")
elif days == 0:
    print("Days must be positive number!")
else:
    if city == "Bansko" or city == "Borovets":
        if package == "withEquipment":
            price = 100
            if vip == "yes":
                price *= 0.9
        elif package == "noEquipment":
            price = 80
            if vip == "yes":
                price *= 0.95
    elif city == "Varna" or city == "Burgas":
        if package == "withBreakfast":
            price = 130
            if vip == "yes":
                price *= 0.88
        elif package == "noBreakfast":
            price = 100
            if vip == "yes":
                price *= 0.93

    total_price = price * days

    print(f"The price is {total_price:.2f}lv! Have a nice time!")