from math import ceil

series_name = str(input())
number_of_seasons = int(input())
number_of_episodes = int(input())
duration_without_adds = float(input())

adds_duration = duration_without_adds / 5
duration_with_adds = duration_without_adds + adds_duration
extra_duration = number_of_seasons * 10
total_time = duration_with_adds * number_of_episodes * number_of_seasons + extra_duration

print(f"Total time needed to watch the {series_name} series is {ceil(total_time)} minutes.")