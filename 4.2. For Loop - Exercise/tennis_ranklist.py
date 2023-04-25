from math import floor

count_tournaments = int(input())
starting_points = int(input())

initial_points = starting_points
points_won = 0
percent_won = 0

for _ in range(1, count_tournaments + 1):
    tournament_stage = input()
    if tournament_stage == "W":
        points_won += 2000
        percent_won += 1
    elif tournament_stage == "F":
        points_won += 1200
    elif tournament_stage == "SF":
        points_won += 720

total_points = points_won + initial_points
average_points = (points_won / count_tournaments)
percent_tournaments_won = (percent_won / count_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_tournaments_won:.2f}%")