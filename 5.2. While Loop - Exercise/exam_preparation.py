count_poor_grades = int(input())

input_line = input()

sum_grades = 0
count_grades = 0
last_problem = ""
number_poor_grades = 0
is_failed = False

while input_line != "Enough":
    problem_name = input_line
    current_grade = int(input())

    if current_grade <= 4:
        number_poor_grades += 1

    if number_poor_grades >= count_poor_grades:
        is_failed = True
        break

    count_grades += 1
    sum_grades += current_grade
    last_problem = problem_name

    input_line = input()

if is_failed:
    print(f"You need a break, {number_poor_grades} poor grades.")
else:
    average_grade = sum_grades / count_grades
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")