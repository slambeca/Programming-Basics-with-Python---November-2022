count_eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

max_color_eggs_number = 0
max_color_eggs_color = 0

for _ in range(1, count_eggs + 1):
    current_egg = input()
    if current_egg == "red":
        red_eggs += 1
    elif current_egg == "orange":
        orange_eggs += 1
    elif current_egg == "blue":
        blue_eggs += 1
    elif current_egg == "green":
        green_eggs += 1

if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs:
    max_color_eggs_number = red_eggs
    max_color_eggs_color = "red"
elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
    max_color_eggs_number = orange_eggs
    max_color_eggs_color = "orange"
elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
    max_color_eggs_number = blue_eggs
    max_color_eggs_color = "blue"
else:
    max_color_eggs_number = green_eggs
    max_color_eggs_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_color_eggs_number} -> {max_color_eggs_color}")

# # Variant 2
# number_of_colored_eggs = int(input())
#
# red_eggs, orange_eggs, green_eggs, blue_eggs = 0, 0, 0, 0
#
# color = 0
#
# for _ in range(number_of_colored_eggs):
#     type_of_egg = input()
#
#     if type_of_egg == "red":
#         red_eggs += 1
#     elif type_of_egg == "orange":
#         orange_eggs += 1
#     elif type_of_egg == "blue":
#         blue_eggs += 1
#     elif type_of_egg == "green":
#         green_eggs += 1
#
# max_number = max(orange_eggs, blue_eggs, green_eggs, red_eggs)
#
# if "green" == max_number:
#     color = "green"
# elif "red" == max_number:
#     color = "red"
# elif "green" == max_number:
#     color = "red"
# elif "blue" == max_number:
#     color = "blue"
#
# print(f"Red eggs: {red_eggs}\nOrange eggs: {orange_eggs}\nBlue eggs: {blue_eggs}\nGreen eggs: {green_eggs}")
# print(f"Max eggs: {max_number} -> {color}")