from math import floor

w = float(input())  # length in meters
h = float(input())  # width in meters

width_without_center_corridor_cm = h * 100 - 100  # = 790

length_in_cm = w * 100  # = 1500 cm

number_of_desks_length = floor(length_in_cm / 120)  # = 12
number_of_desks_width = floor(width_without_center_corridor_cm / 70)  # = 11

total_number_of_desks = number_of_desks_length * number_of_desks_width - 3
print(total_number_of_desks)