first_number = int(input())
second_number = int(input())
third_number = int(input())

for x in range(2, first_number + 1, 2):
    for y in range(2, second_number + 1):
        for z in range(2, third_number + 1, 2):
            if y == 2 or y == 3 or y == 5 or y == 7:
                print(f"{x} {y} {z}")