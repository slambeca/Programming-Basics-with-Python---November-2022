number_guests = int(input())
price_for_guest = float(input())
budget = float(input())

if number_guests < 10:
    price_for_guest *= 1
elif 10 <= number_guests <= 15:
    price_for_guest *= 0.85
elif 15 < number_guests <= 20:
    price_for_guest *= 0.8
else:
    price_for_guest *= 0.75

price_cake = budget * 0.1
total_spendings = number_guests * price_for_guest + price_cake

if total_spendings <= budget:
    print(f"It is party time! {budget - total_spendings:.2f} leva left.")
else:
    print(f"No party! {total_spendings - budget:.2f} leva needed.")