holidays = int(input())

working_days = 365 - holidays
total_play_minutes = working_days * 63 + holidays * 127
difference = abs(total_play_minutes - 30000)  # to remove the minus sign, also we can use math.fabs, which returns float

hours = difference // 60
minutes = difference % 60

if total_play_minutes < 30000:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")