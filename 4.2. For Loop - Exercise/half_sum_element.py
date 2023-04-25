import sys

number = int(input())

max_number = -sys.maxsize
total_sum = 0
others_sum = 0

for num in range(number):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

    total_sum += current_number

others_sum = total_sum - max_number

if total_sum - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - others_sum)}")