number = int(input())

current_pair_sum = 0
previous_pair_sum = 0
max_diff_pair = 0

for i in range(number * 2):
    current_number = int(input())
    current_pair_sum += current_number

    if i % 2 != 0 and i >= 3:
        max_diff_pair = max(max_diff_pair, abs(current_pair_sum - previous_pair_sum))
        previous_pair_sum = current_pair_sum
        current_pair_sum = 0

    elif i % 2 != 0 and i >= 1:
        previous_pair_sum = current_pair_sum
        current_pair_sum = 0

if max_diff_pair == 0:
    print(f"Yes, value={previous_pair_sum}")
else:
    print(f"No, maxdiff={max_diff_pair}")