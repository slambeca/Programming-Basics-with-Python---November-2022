days = int(input())
type_room = input()
rating = input()

total_price = None
number_of_nights = days - 1

price_room_for_one = 18
price_apartment = 25
price_president_apartment = 35

if type_room == "room for one person":
    total_price = price_room_for_one * number_of_nights
elif type_room == "apartment":
    if days < 10:
        total_price = (price_apartment * number_of_nights) * 0.7
    elif 10 <= days <= 15:
        total_price = (price_apartment * number_of_nights) * 0.65
    else:
        total_price = (price_apartment * number_of_nights) * 0.5
else:
    if days < 10:
        total_price = (price_president_apartment * number_of_nights) * 0.9
    elif 10 <= days <= 15:
        total_price = (price_president_apartment * number_of_nights) * 0.85
    else:
        total_price = (price_president_apartment * number_of_nights) * 0.8

if rating == "positive":
    total_price *= 1.25
else:
    total_price *= 0.9

print(f"{total_price:.2f}")