moves = int(input())

points = 0

group_one = 0
group_two = 0
group_three = 0
group_four = 0
group_five = 0

invalid_numbers = 0

for _ in range(1, moves + 1):
    current_number = int(input())
    if 0 <= current_number <= 9:
        points += current_number * 0.2
        group_one += 1
    elif 10 <= current_number <= 19:
        points += current_number * 0.3
        group_two += 1
    elif 20 <= current_number <= 29:
        points += current_number * 0.4
        group_three += 1
    elif 30 <= current_number <= 39:
        points += 50
        group_four += 1
    elif 40 <= current_number <= 50:
        points += 100
        group_five += 1
    else:
        points /= 2
        invalid_numbers += 1

percent_group_one = (group_one / moves) * 100
percent_group_two = (group_two / moves) * 100
percent_group_three = (group_three / moves) * 100
percent_group_four = (group_four / moves) * 100
percent_group_five = (group_five / moves) * 100
percent_invalid = (invalid_numbers / moves) * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percent_group_one:.2f}%")
print(f"From 10 to 19: {percent_group_two:.2f}%")
print(f"From 20 to 29: {percent_group_three:.2f}%")
print(f"From 30 to 39: {percent_group_four:.2f}%")
print(f"From 40 to 50: {percent_group_five:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")