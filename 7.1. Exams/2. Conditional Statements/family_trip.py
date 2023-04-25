budget = float(input())
number_nights = int(input())
price_for_night = float(input())
percent_additional_spending = int(input())

if number_nights > 7:
    price_for_night = price_for_night * 0.95

sum_paid = number_nights * price_for_night
additional_spending = percent_additional_spending / 100 * budget

total_sum = sum_paid + additional_spending

if total_sum <= budget:
    print(f"Ivanovi will be left with {budget - total_sum:.2f} leva after vacation.")
else:
    print(f"{total_sum - budget:.2f} leva needed.")