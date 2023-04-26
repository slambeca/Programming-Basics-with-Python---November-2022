seats_in_hall = int(input())

input_line = input()

seats_left = seats_in_hall

revenue = 0

while input_line != "Movie time!":
    count_people = int(input_line)
    seats_left -= count_people

    revenue += (count_people * 5)

    if seats_left < 0:
        print(f"The cinema is full.")
        revenue -= count_people * 5
        break

    if count_people % 3 == 0:
        revenue -= 5

    input_line = input()

else:
    print(f"There are {seats_left} seats left in the cinema.")

print(f"Cinema income - {revenue} lv. ")