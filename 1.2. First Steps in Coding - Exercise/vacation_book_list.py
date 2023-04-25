number_of_pages = int(input())
pages_an_hour = int(input())
number_of_days = int(input())

total_time = number_of_pages / pages_an_hour    # or we can write number_of_pages // pages_an_hour
hours_needed = total_time / number_of_days    # or we can write total_time // number_of_days
print(int(hours_needed))    # this is not recommended, we should use //