age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_count = 0
total_sum = 0
money = 10
brother_money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        total_sum += money
        money = money + 10
        brother_money += 1
    elif year % 2 == 1:
        toy_count += 1

total_sum = total_sum + toy_price * toy_count - brother_money

if total_sum >= washing_machine_price:
    print(f"Yes! {total_sum - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_sum:.2f}")