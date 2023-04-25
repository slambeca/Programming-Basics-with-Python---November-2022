width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

sum_all_boxes = 0

input_line = input()

while input_line != "Done":
    boxes = int(input_line)

    sum_all_boxes += boxes

    if sum_all_boxes >= volume:
        break

    input_line = input()

diff = abs(volume - sum_all_boxes)

if sum_all_boxes >= volume:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")