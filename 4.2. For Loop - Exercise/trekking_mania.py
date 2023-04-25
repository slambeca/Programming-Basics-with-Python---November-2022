group_count = int(input())

peak_one = 0
peak_two = 0
peak_three = 0
peak_four = 0
peak_five = 0

total_people = 0

for _ in range(group_count):
    people_in_group = int(input())
    if people_in_group <= 5:
        peak_one += people_in_group
    elif people_in_group <= 12:
        peak_two += people_in_group
    elif people_in_group <= 25:
        peak_three += people_in_group
    elif people_in_group <= 40:
        peak_four += people_in_group
    elif people_in_group >= 41:
        peak_five += people_in_group

total_people = peak_one + peak_two + peak_three + peak_four + peak_five

print(f"{(peak_one / total_people) * 100:.2f}%")
print(f"{(peak_two / total_people) * 100:.2f}%")
print(f"{(peak_three / total_people) * 100:.2f}%")
print(f"{(peak_four / total_people) * 100:.2f}%")
print(f"{(peak_five / total_people) * 100:.2f}%")