import math

number_of_people = int(input())
entry_fee = float(input())
sun_lounger = float(input())
umbrella_fee = float(input())

entry_fee_total = number_of_people * entry_fee
price_of_sun_lounger = math.ceil(number_of_people * 0.75) * sun_lounger
price_of_umbrella = math.ceil(number_of_people / 2) * umbrella_fee

total_sum = entry_fee_total + price_of_umbrella + price_of_sun_lounger

formatted_total_sum = '{:.2f} lv.'.format(total_sum)

print(formatted_total_sum)

# Variant 2
# from math import ceil
#
# total_people, tax_entrance, sun_bed_price, umbrella_price = int(input()), float(input()), float(input()),
# float(input())
#
# total_price_entrance = total_people * tax_entrance
# total_price_sun_beds = ceil(total_people * 0.75) * sun_bed_price
# total_price_for_umbrellas = (umbrella_price * ceil(total_people / 2))
#
# final_price = total_price_entrance + total_price_sun_beds + total_price_for_umbrellas
#
# print(f"{final_price:.2f} lv.")