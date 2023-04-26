price_jersey = float(input())
needed_sum = float(input())

price_shorts = price_jersey * 0.75
price_socks = price_shorts * 0.2
price_kicks = (price_jersey + price_shorts) * 2

discount = 85/100

total_price = price_jersey + price_shorts + price_socks + price_kicks

total_price_with_discount = total_price * discount

if total_price_with_discount >= needed_sum:
    print(f"Yes, he will earn the world-cup replica ball!\nHis sum is {total_price_with_discount:.2f} lv.")
else:
    print(f"No, he will not earn the world cup replica ball.\nHe needs "
          f"{abs(needed_sum - total_price_with_discount):.2f} lv. more.")