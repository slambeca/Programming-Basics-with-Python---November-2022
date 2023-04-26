from math import ceil

height = int(input())
width = int(input())
percent_without_paint = int(input())

walls_total = height * width * 4

walls_total *= (100 - percent_without_paint) / 100

input_line = input()

while input_line != "Tired!":
    liters_used = int(input_line)

    walls_total -= liters_used

    if walls_total < 0:
        print(f"All walls are painted and you have {abs(ceil(walls_total))} l paint left!")
        break
    elif walls_total == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break

    input_line = input()

else:
    print(f"{ceil(walls_total)} quadratic m left.")