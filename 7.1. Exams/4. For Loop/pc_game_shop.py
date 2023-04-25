games_sold = int(input())

hearthstone_sold = 0
fortnite_sold = 0
overwatch_sold = 0
others_sold = 0

for _ in range(1, games_sold + 1):
    current_game = input()
    if current_game == "Hearthstone":
        hearthstone_sold += 1
    elif current_game == "Fortnite":
        fortnite_sold += 1
    elif current_game == "Overwatch":
        overwatch_sold += 1
    else:
        others_sold += 1

print(f"Hearthstone - {(hearthstone_sold / games_sold) * 100:.2f}%")
print(f"Fortnite - {(fortnite_sold / games_sold) * 100:.2f}%")
print(f"Overwatch - {(overwatch_sold / games_sold) * 100:.2f}%")
print(f"Others - {(others_sold / games_sold) * 100:.2f}%")