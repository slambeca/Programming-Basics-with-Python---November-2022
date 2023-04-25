season = input()
group_type = input()
student_number = int(input())
nights = int(input())

price = None
sport = None

if group_type == "boys":
    if season == "Winter":
        price = 9.60 * student_number
        sport = "Judo"
    elif season == "Spring":
        price = 7.20 * student_number
        sport = "Tennis"
    else:
        price = 15 * student_number
        sport = "Football"
elif group_type == "girls":
    if season == "Winter":
        price = 9.60 * student_number
        sport = "Gymnastics"
    elif season == "Spring":
        price = 7.20 * student_number
        sport = "Athletics"
    else:
        price = 15 * student_number
        sport = "Volleyball"
else:
    if season == "Winter":
        price = 10 * student_number
        sport = "Ski"
    elif season == "Spring":
        price = 9.5 * student_number
        sport = "Cycling"
    else:
        price = 20 * student_number
        sport = "Swimming"

price *= nights

if student_number >= 50:
    price *= 0.5
elif 20 <= student_number < 50:
    price *= 0.85
elif 10 <= student_number < 20:
    price *= 0.95

print(f"{sport} {price:.2f} lv.")