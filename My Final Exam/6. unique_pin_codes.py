end_of_first_range = int(input())
end_of_second_range = int(input())
end_of_third_range = int(input())

for x in range(1, end_of_first_range + 1):
    if x % 2 == 0:
        for y in range(1, end_of_second_range + 1):
            if y == 2 or y == 3 or y == 5 or y == 7:
                for z in range(1, end_of_third_range + 1):
                    if z % 2 == 0:
                        print(f"{x} {y} {z}")