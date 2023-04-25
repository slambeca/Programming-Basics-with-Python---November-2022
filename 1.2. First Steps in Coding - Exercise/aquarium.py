# 1 liter of water equals 1 cubic decimeter
length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage_with_accessories = float(input())

aquarium_volume = length_cm * width_cm * height_cm
volume_in_liters = aquarium_volume * 0.001

volume_with_no_watter = percentage_with_accessories / 100
water_needed_lt = volume_in_liters * (1 - volume_with_no_watter)

print(water_needed_lt)