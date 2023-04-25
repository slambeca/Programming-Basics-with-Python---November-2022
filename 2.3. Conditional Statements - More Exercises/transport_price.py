distance = int(input())
time_of_day = (input())

price = 0
taxi_rate = 0

if time_of_day == "day":
    taxi_rate = distance * 0.79 + 0.7
else:
    taxi_rate = distance * 0.9 + 0.7

if distance < 20:
    price = taxi_rate
elif distance < 100:
    price = distance * 0.09
else:
    price = distance * 0.06

print(f"{price:.2f}")