football_team = input()
matches = int(input())

points = 0
games_won = 0
games_draw = 0
games_lost = 0

for _ in range(1, matches + 1):
    current_result = input()
    if current_result == "W":
        points += 3
        games_won += 1
    elif current_result == "D":
        points += 1
        games_draw += 1
    elif current_result == "L":
        points += 0
        games_lost += 1

if matches == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {games_won}")
    print(f"## D: {games_draw}")
    print(f"## L: {games_lost}")
    print(f"Win rate: {(games_won / matches) * 100:.2f}%")