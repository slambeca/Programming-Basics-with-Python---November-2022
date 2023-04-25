from math import ceil

series_name = input()
series_duration = int(input())
lunch_break_duration = int(input())

lunch_duration = lunch_break_duration / 8
recreation_time = lunch_break_duration / 4

time_for_watching_series = lunch_break_duration - (lunch_duration + recreation_time)

if time_for_watching_series >= series_duration:
    print(
        f"You have enough time to watch {series_name} and left with {ceil(time_for_watching_series - series_duration)} "
        f"minutes free time.")
else:
    print(
        f"You don't have enough time to watch {series_name}, you need {ceil(series_duration - time_for_watching_series)} "
        f"more minutes.")