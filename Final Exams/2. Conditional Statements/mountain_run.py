from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_climbing_one_meter = float(input())

time_for_climbing = distance_in_meters * time_for_climbing_one_meter
delay_in_seconds = floor(distance_in_meters / 50) * 30
total_time = time_for_climbing + delay_in_seconds

if record_in_seconds <= total_time:
    print(f"No! He was {total_time - record_in_seconds:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")