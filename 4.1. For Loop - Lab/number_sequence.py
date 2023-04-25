import sys

number = int(input())

# -9223372036854775807 - even if we find a number bigger with one, it will be our new max number
# -9223372036854775806 - this number is bigger
max_number = -sys.maxsize

# 9223372036854775807 - even if we find a number smaller with one, it will be our new min number
# 9223372036854775806 - this number is smaller
min_number = sys.maxsize

for num in range(number):
    current_number = (int(input()))

    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print("Max number: " + str(max_number))
print("Min number: " + str(min_number))