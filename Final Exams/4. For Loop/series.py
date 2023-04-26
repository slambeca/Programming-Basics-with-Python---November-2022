budget = float(input())
count_series = int(input())

total_sum = 0

for _ in range(1, count_series + 1):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        series_price *= 0.5
    elif series_name == "Lucifer":
        series_price *= 0.6
    elif series_name == "Protector":
        series_price *= 0.7
    elif series_name == "TotalDrama":
        series_price *= 0.8
    elif series_name == "Area":
        series_price *= 0.9
    else:
        series_price = series_price

    total_sum += series_price

if budget >= total_sum:
    print(f"You bought all the series and left with {budget - total_sum:.2f} lv.")
else:
    print(f"You need {total_sum - budget:.2f} lv. more to buy the series!")