from math import ceil

days_of_training = int(input())
kilometers_run_on_day_one = int(input())

total_kilometers_run = kilometers_run_on_day_one

final_kilometers_run = total_kilometers_run

for _ in range(days_of_training):
    percent_kilometers_added = int(input())

    total_kilometers_run += (total_kilometers_run * percent_kilometers_added / 100)

    final_kilometers_run += total_kilometers_run

diff = abs(1000 - final_kilometers_run)

if final_kilometers_run >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")