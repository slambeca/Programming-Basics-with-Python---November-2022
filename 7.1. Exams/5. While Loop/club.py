wanted_revenue = float(input())

club_income = 0

price = 0

input_line = input()

while input_line != "Party!":
    cocktail = input_line
    count_cocktails = int(input())

    price = len(cocktail) * count_cocktails

    if price % 2 == 1:
        price *= 0.75

    club_income += price

    if club_income >= wanted_revenue:
        print(f"Target acquired.")
        break

    input_line = input()

else:
    print(f"We need {wanted_revenue - club_income:.2f} leva more.")

print(f"Club income - {club_income:.2f} leva.")