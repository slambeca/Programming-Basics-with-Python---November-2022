name_of_player = input()

best_player = ""
best_score = 0
is_hatrick = False

while name_of_player != "END":
    goals_scored = int(input())
    if goals_scored > best_score:
        best_score = goals_scored
        best_player = name_of_player
        if best_score >= 3:
            is_hatrick = True

    if best_score >= 10:
        break

    name_of_player = input()

print(f"{best_player} is the best player!")

if is_hatrick:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_score} goals.")