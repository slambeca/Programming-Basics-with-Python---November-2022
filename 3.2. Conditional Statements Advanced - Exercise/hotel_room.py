month = input()
num_nights = int(input())

total_sum_apartment = None
total_sum_studio = None

price_apartment = 0
price_studio = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if 7 < num_nights <= 14:
        price_studio = price_studio * 0.95
    elif num_nights > 14:
        price_studio *= 0.7
        price_apartment *= 0.9
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if num_nights > 14:
        price_studio *= 0.8
        price_apartment *= 0.9
else:
    price_studio = 76
    price_apartment = 77
    if num_nights > 14:
        price_apartment *= 0.9

total_sum_apartment = num_nights * price_apartment
total_sum_studio = num_nights * price_studio

print(f"Apartment: {total_sum_apartment:.2f} lv.")
print(f"Studio: {total_sum_studio:.2f} lv.")