chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

price_chrysanthemums = None
price_roses = None
price_tulips = None
total_price = None

if season == "Spring" or season == "Summer":
    price_chrysanthemums = 2.00 * chrysanthemums
    price_roses = 4.10 * roses
    price_tulips = 2.50 * tulips
    total_price = price_chrysanthemums + price_roses + price_tulips
    if tulips > 7:
        total_price *= 0.95
elif season == "Autumn":
    price_chrysanthemums = 3.75 * chrysanthemums
    price_roses = 4.50 * roses
    price_tulips = 4.15 * tulips
    total_price = price_chrysanthemums + price_roses + price_tulips
elif season == "Winter":
    price_chrysanthemums = 3.75 * chrysanthemums
    price_roses = 4.50 * roses
    price_tulips = 4.15 * tulips
    total_price = price_chrysanthemums + price_roses + price_tulips
    if roses >= 10:
        total_price *= 0.9

if holiday == "Y":
    total_price *= 1.15

if (chrysanthemums + roses + tulips) > 20:
    total_price *= 0.8

print(f"{total_price + 2:.2f}")