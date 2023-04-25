n = int(input())

left_sum = 0
right_sum = 0

for number in range(0, n*2):    # the middle part of a range is something abstract
    current_number = int(input())
    if number < n:
        left_sum += current_number
    elif number >= n:
        right_sum += current_number

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {diff}")