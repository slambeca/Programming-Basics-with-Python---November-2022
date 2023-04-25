num = int(input())

for i in range(1, 10):  # do not include 0 in the range, because we cannot divide by 0
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                is_valid = num % i == 0 and num % j == 0 and num % k == 0 and num % l == 0
                if is_valid:
                    print(f"{i}{j}{k}{l}", end=" ")

# # Variant 2
# number = int(input())
#
# for a in range(1, 10):
#     for b in range(1, 10):
#         for c in range(1, 10):
#             for d in range(1, 10):
#                 if number % a == 0 and number % b == 0 and number % c == 0 and number % d == 0:
#                     print(f"{a}{b}{c}{d}", end=" ")
