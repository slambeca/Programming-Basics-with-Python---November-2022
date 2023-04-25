students = int(input())

group_one = 0
group_two = 0
group_three = 0
group_four = 0

average_from_groups = 0

for _ in range(1, students + 1):
    current_grade = float(input())
    if current_grade < 3.00:
        group_one += 1
    elif current_grade < 4.00:
        group_two += 1
    elif current_grade < 5.00:
        group_three += 1
    elif current_grade >= 5.00:
        group_four += 1

    average_from_groups += current_grade

print(f"Top students: {(group_four / students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(group_three / students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(group_two / students) * 100:.2f}%")
print(f"Fail: {(group_one / students) * 100:.2f}%")
print(f"Average: {average_from_groups / students:.2f}")