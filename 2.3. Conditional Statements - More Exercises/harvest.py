from math import floor, ceil

square_meters_land = int(input())
grape_for_square_meter = float(input())
needed_lts_wine = int(input())
number_workers = int(input())

total_grape = square_meters_land * grape_for_square_meter
wine = 0.4 * total_grape / 2.5
wine_left = wine - needed_lts_wine

if wine >= needed_lts_wine:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(round(wine_left, 0) / number_workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(needed_lts_wine - wine)} liters wine needed.")