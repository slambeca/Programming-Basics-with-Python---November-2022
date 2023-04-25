hour = int(input())
minutes = int(input())

total_minutes = hour * 60 + minutes
total_minutes += 15

hours = total_minutes // 60
minutes = total_minutes % 60

if hours == 24:
    hours -= 24

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")