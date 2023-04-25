season = input()
km_per_month = float(input())

salary = None

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = 0.75 * km_per_month
    elif season == "Summer":
        salary = 0.9 * km_per_month
    elif season == "Winter":
        salary = 1.05 * km_per_month
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = 0.95 * km_per_month
    elif season == "Summer":
        salary = 1.1 * km_per_month
    elif season == "Winter":
        salary = 1.25 * km_per_month
elif 10000 < km_per_month <= 20000:
    salary = 1.45 * km_per_month

salary = salary * 0.9 * 4

print(f"{salary:.2f}")