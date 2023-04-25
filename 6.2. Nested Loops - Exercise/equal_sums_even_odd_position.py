first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number + 1):
    current_number_string = str(i)      # when we want the digits at each position, we convert it
    # to string and use its indexes
    even_sum = 0
    odd_sum = 0
    for j in range(0, len(current_number_string)):
        digit = int(current_number_string[j])
        if j % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(current_number_string, end=" ")

# Variant 2
# first_number = int(input())
# second_number = int(input())
#
# for each_number in range(first_number, second_number + 1):
#     current_number_as_string = str(each_number)
#     even_sum = 0
#     odd_sum = 0
#     # 100000
#     for each_position in range(0, 6): # or len(current_number_as_string)
#         digit = int(current_number_as_string[each_position])
#
#         if each_position % 2 == 0:
#             even_sum += digit
#         else:
#             odd_sum += digit
#
#     if even_sum == odd_sum:
#         print(current_number_as_string, end=" ")