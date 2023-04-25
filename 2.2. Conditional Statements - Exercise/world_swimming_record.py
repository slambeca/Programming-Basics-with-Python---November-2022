from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_one_meter = float(input())

time_for_distance = distance_in_meters * seconds_for_one_meter + floor(distance_in_meters / 15) * 12.5
# we can use distance_in_meters // 15

if time_for_distance >= record_in_seconds:
    print(f"No, he failed! He was {time_for_distance - record_in_seconds:.2f} seconds slower.")
elif time_for_distance < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {time_for_distance:.2f} seconds.")