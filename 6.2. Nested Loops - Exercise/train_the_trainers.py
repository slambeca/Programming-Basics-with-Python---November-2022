count_judges = int(input())

input_line = input()

count_grades = 0
sum_total_grades = 0

while input_line != "Finish":
    presentation = input_line

    sum_current_grades = 0
    current_average_grade = 0

    for _ in range(count_judges):
        current_grade = float(input())

        count_grades += 1
        sum_total_grades += current_grade
        sum_current_grades += current_grade

        current_average_grade = sum_current_grades / count_judges

    print(f"{presentation} - {current_average_grade:.2f}.")

    input_line = input()

print(f"Student's final assessment is {sum_total_grades / count_grades:.2f}.")