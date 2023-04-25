name = input()

grades_total = 0
years_counter = 0
failed_years = 0

while True:
    annual_grade = float(input())
    years_counter += 1

    if annual_grade < 4.00:
        failed_years += 1

        if failed_years == 2:
            print(f"{name} has been excluded at {years_counter} grade")
            break

        years_counter -= 1

    else:
        grades_total += annual_grade

    if years_counter == 12:
        average_grade = grades_total / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break

# Variant 2
# name = input()
#
# years_passed = 0
# years_failed = 0
# sum_of_all_grades = 0
#
# while True:
#     current_grade = float(input())
#     years_passed += 1
#
#     if current_grade < 4.00:
#         years_failed += 1
#
#         if years_failed == 2:
#             print(f"{name} has been excluded at {years_passed} grade")
#             break
#
#         years_passed -= 1
#
#     else:
#         sum_of_all_grades += current_grade
#
#     if years_passed == 12:
#         average_grade = sum_of_all_grades / 12
#         print(f"{name} graduated. Average grade: {average_grade:.2f}")
#         break