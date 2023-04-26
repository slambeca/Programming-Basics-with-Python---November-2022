from math import floor

number = int(input())

points = 0

red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_color_balls = 0

divides_black_balls = 0

for _ in range(1, number + 1):
    current_color = input()
    if current_color == "red":
        points += 5
        red_balls += 1
    elif current_color == "orange":
        points += 10
        orange_balls += 1
    elif current_color == "yellow":
        points += 15
        yellow_balls += 1
    elif current_color == "white":
        points += 20
        white_balls += 1
    elif current_color == "black":
        points = floor(points / 2)
        black_balls += 1
        divides_black_balls += 1
    else:
        other_color_balls += 1

print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_color_balls}")
print(f"Divides from black balls: {divides_black_balls}")