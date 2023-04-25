from math import ceil

number_guests = int(input())
budget = int(input())

easter_breads_needed = ceil(number_guests / 3)
eggs_needed = number_guests * 2
paid_for_easter_breads = easter_breads_needed * 4
paid_for_eggs = eggs_needed * 0.45
total_paid = paid_for_easter_breads + paid_for_eggs

if total_paid <= budget:
    print(f"Lyubo bought {easter_breads_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {budget - total_paid:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_paid - budget:.2f} lv. more.")