input_line = input()

hattrick = False

best_score = 0
best_player = ""

while input_line != "END":
    player_name = input_line

    goals_scored = int(input())

    if goals_scored > best_score:
        best_score = goals_scored
        best_player = player_name

    if goals_scored >= 3:
        hattrick = True

    if goals_scored >= 10:
        hattrick = True
        break

    input_line = input()

print(f"{best_player} is the best player!")

if hattrick:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score} goals.")