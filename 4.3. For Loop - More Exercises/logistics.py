count_shipments = int(input())

total_weight = 0

microbus_tones = 0
truck_tones = 0
train_tones = 0

average_price = 0

for _ in range(1, count_shipments + 1):
    current_weight = int(input())
    total_weight += current_weight
    if current_weight <= 3:
        microbus_tones += current_weight
    elif 4 <= current_weight <= 11:
        truck_tones += current_weight
    elif current_weight >= 12:
        train_tones += current_weight

    average_price += current_weight

average_price = (microbus_tones * 200 + truck_tones * 175 + train_tones * 120) / total_weight

microbus_percentage = (microbus_tones / total_weight) * 100
truck_percentage = (truck_tones / total_weight) * 100
train_percentage = (train_tones / total_weight) * 100

print(f"{average_price:.2f}")
print(f"{microbus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")