inherited_money = float(input())
year = int(input())

age = 18
money_left = inherited_money

for num in range(1800, year + 1):
    if num % 2 == 0:
        money_left -= 12000
    else:
        money_left -= 12000 + (50 * age)

    age += 1

if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")