name_p1 = input()
name_p2 = input()

points_p1 = 0
points_p2 = 0

input_text = input()

while input_text != "End of game":
    card_p1 = int(input_text)
    card_p2 = int(input())

    if card_p1 > card_p2:
        points_p1 += (card_p1 - card_p2)

    if card_p2 > card_p1:
        points_p2 += (card_p2 - card_p1)

    if card_p1 == card_p2:
        print("Number wars!")
        card_p1 = int(input())
        card_p2 = int(input())

        if card_p1 > card_p2:
            print(f"{name_p1} is winner with {points_p1} points")
            break
        elif card_p2 > card_p1:
            print(f"{name_p2} is winner with {points_p2} points")
            break

    input_text = input()

if input_text == "End of game":
    print(f"{name_p1} has {points_p1} points")
    print(f"{name_p2} has {points_p2} points")