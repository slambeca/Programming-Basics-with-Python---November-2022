input_line = input()

prime_sum = 0
non_prime_sum = 0

while input_line != "stop":
    current_number = int(input_line)   # 3

    if current_number < 0:
        print(f"Number is negative.")
        input_line = input()
        continue

    count_divisors = 0   # number of divisors of a number

    for i in range(1, current_number + 1):  # or use 2 as starting point and if we find only 1 divisor, it`s prime num
        # 3 // 1   3 // 2   3 // 3
        if current_number % i == 0:
            count_divisors += 1

    if count_divisors == 2:
        prime_sum += current_number
    else:
        non_prime_sum += current_number

    input_line = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")

# # Variant 2
# input_line = input()
#
# prime_sum = 0
# non_prime_sum = 0
#
# while input_line != "stop":
#     current_number = int(input_line)   # 3
#
#     if current_number < 0:
#         print(f"Number is negative.")
#     else:
#         count_divisors = 0   # number of divisors of a number
#
#         for i in range(1, current_number + 1):
#             # 3 // 1   3 // 2   3 // 3
#             if current_number % i == 0:
#                 count_divisors += 1
#
#         if count_divisors == 2:
#             prime_sum += current_number
#         else:
#             non_prime_sum += current_number
#
#         input_line = input()
#
# print(f"Sum of all prime numbers is: {prime_sum}")
# print(f"Sum of all non prime numbers is: {non_prime_sum}")