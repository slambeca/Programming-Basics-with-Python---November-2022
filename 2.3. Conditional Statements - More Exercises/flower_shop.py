from math import ceil, floor

number_magnolias = int(input())
number_hyacinths = int(input())
number_roses = int(input())
number_cacti = int(input())
gift_price = float(input())

paid_for_magnolias = number_magnolias * 3.25
paid_for_hyacinths = number_hyacinths * 4
paid_for_roses = number_roses * 3.5
paid_for_cacti = number_cacti * 8

total = paid_for_magnolias + paid_for_hyacinths + paid_for_roses + paid_for_cacti
tax = total / 20
revenue = total - tax

if gift_price > revenue:
    print(f"She will have to borrow {ceil(gift_price - revenue)} leva.")
else:
    print(f"She is left with {floor(revenue - gift_price)} leva.")