length = int(input())
width = int(input())

total_pieces = length * width

pieces_taken = 0

cake_is_done = False

input_line = input()

while input_line != "STOP":
    pieces = int(input_line)

    pieces_taken += pieces

    if pieces_taken >= total_pieces:
        cake_is_done = True
        break

    input_line = input()

diff = abs(total_pieces - pieces_taken)

if cake_is_done:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")