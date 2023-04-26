hall_fee = int(input())

statues_price = hall_fee - (hall_fee * 0.30)
catering_price = statues_price * 0.85
sound_over_price = catering_price / 2

total_sum = hall_fee + statues_price + catering_price + sound_over_price

print(f"{total_sum:.2f}")