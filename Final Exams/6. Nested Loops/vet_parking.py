days = int(input())
hours_per_day = int(input())

total_price = 0
price_per_day = 0

for day in range(1, days + 1):
    if day > 1:
        print(f'Day: {day - 1} - {price_per_day:.2f} leva')
    total_price += price_per_day
    price_per_day = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and not hour % 2 == 0:
            price_per_day += 2.50
        elif not day % 2 == 0 and hour % 2 == 0:
            price_per_day += 1.25
        else:
            price_per_day += 1

total_price += price_per_day
print(f'Day: {day} - {price_per_day:.2f} leva')
print(f'Total: {total_price:.2f} leva')