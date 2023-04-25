trip_price = float(input())
puzzles = int(input())
speaking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
lorries = int(input())

total_toys = puzzles + speaking_dolls + teddy_bears + minions + lorries

revenue = puzzles * 2.6 + speaking_dolls * 3 + teddy_bears * 4.1 + \
          minions * 8.2 + lorries * 2

if total_toys >= 50:
    revenue = revenue - (revenue * 0.25)

rent_price = revenue * 0.1

revenue -= rent_price

if revenue >= trip_price:
    print(f"Yes! {revenue - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {abs(revenue - trip_price):.2f} lv needed.")