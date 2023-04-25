number = int(input())

first_digit = number % 10
second_digit = number // 10 % 10
third_digit = number // 100 % 10

for num1 in range(1, first_digit + 1):
    for num2 in range(1, second_digit + 1):
        for num3 in range(1, third_digit + 1):
            result = num1 * num2 * num3
            print(f"{num1} * {num2} * {num3} = {result};")

# # Variant 2
# n = int(input())
#
# for x3 in range(1, n % 10 + 1):
#     for x2 in range(1, (n // 10) % 10 + 1):
#         for x1 in range(1, n // 100 + 1):
#             print(f"{x3} * {x2} * {x1} = {x1 * x2 * x3};")