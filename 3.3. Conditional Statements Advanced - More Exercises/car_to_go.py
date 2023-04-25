budget = float(input())
season = input()

car_type = None
car_class = None
price = None

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        price = budget * 0.35
        car_type = "Cabrio"
    elif season == "Winter":
        price = budget * 0.65
        car_type = "Jeep"
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        price = budget * 0.45
        car_type = "Cabrio"
    elif season == "Winter":
        price = budget * 0.80
        car_type = "Jeep"
elif budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.9

print(f"{car_class}")
print(f"{car_type} - {price:.2f}")