stadium_capacity = int(input())
count_fans = int(input())

fans_sector_a = 0
fans_sector_b = 0
fans_sector_v = 0
fans_sector_g = 0

fans_total = 0

for _ in range(1, count_fans + 1):
    current_sector = input()
    if current_sector == "A":
        fans_sector_a += 1
    elif current_sector == "B":
        fans_sector_b += 1
    elif current_sector == "V":
        fans_sector_v += 1
    elif current_sector == "G":
        fans_sector_g += 1

    fans_total += 1

percent_sector_a = (fans_sector_a / count_fans) * 100
percent_sector_b = (fans_sector_b / count_fans) * 100
percent_sector_v = (fans_sector_v / count_fans) * 100
percent_sector_g = (fans_sector_g / count_fans) * 100

percent_fans_total = (fans_total / stadium_capacity) * 100

print(f"{percent_sector_a:.2f}%")
print(f"{percent_sector_b:.2f}%")
print(f"{percent_sector_v:.2f}%")
print(f"{percent_sector_g:.2f}%")
print(f"{percent_fans_total:.2f}%")