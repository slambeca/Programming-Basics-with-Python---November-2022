first_number = int(input())
second_number = int(input())
third_number = int(input())

for x in range(2, first_number + 1, 2):
    for y in range(second_number + 1):
        for z in range(2, third_number + 1, 2):
            if y == 2 or y == 3 or y == 5 or y == 7:
                print(f"{x} {y} {z}")

# # Variant 2
# a = int(input())
# b = int(input())
# c = int(input())
#
# for i in range(1, a+1):
#     if i % 2 == 0:
#         for j in range(2, b+1):
#             if j == 2 or j == 3 or j == 5 or j == 7:
#                 for k in range(1, c+1):
#                     if k % 2 == 0:
#                         print(f'{i} {j} {k}')