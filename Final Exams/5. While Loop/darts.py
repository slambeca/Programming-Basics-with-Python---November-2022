starting_points = 301

player_name = input()
input_line = input()

unsuccessful_shots = 0
successful_shots = 0

while input_line != "Retire":
    sector = input_line
    points = int(input())

    if sector == "Single":
        points *= 1
    elif sector == "Double":
        points *= 2
    elif sector == "Triple":
        points *= 3

    if points > starting_points:
        unsuccessful_shots += 1
    else:
        starting_points -= points
        successful_shots += 1

    if starting_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break

    input_line = input()

else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")

# # Variant 2
# player_name = input()
#
# successful_shots = 0
# unsuccessful_shots = 0
#
# points = 301
#
# while points > 0:
#     command = input()
#
#     if command == "Retire":
#         print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
#         break
#
#     current_points = int(input())
#
#     if command == "Single":
#         pass
#     elif command == "Double":
#         current_points *= 2
#     elif command == "Triple":
#         current_points *= 3
#
#     if current_points > points:
#         unsuccessful_shots += 1
#         continue
#     else:
#         points -= current_points
#         successful_shots += 1
#
# if points == 0:
#     print(f"{player_name} won the leg with {successful_shots} shots.")