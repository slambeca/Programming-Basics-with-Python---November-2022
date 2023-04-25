eggs_p1 = int(input())
eggs_p2 = int(input())

total_eggs_player_one = eggs_p1
total_eggs_player_two = eggs_p2

command = input()

while command != "End":
    if command == "one":
        total_eggs_player_two -= 1
        if total_eggs_player_two <= 0:
            print(f"Player two is out of eggs. Player one has {total_eggs_player_one} eggs left.")
            break
    elif command == "two":
        total_eggs_player_one -= 1
        if total_eggs_player_one <= 0:
            print(f"Player one is out of eggs. Player two has {total_eggs_player_two} eggs left.")
            break

    command = input()

else:
    print(f"Player one has {total_eggs_player_one} eggs left.")
    print(f"Player two has {total_eggs_player_two} eggs left.")