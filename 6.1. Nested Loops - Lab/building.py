floors = int(input())
flats_per_floor = int(input())

flat_name = 0

for floor_n in range(floors, 0, -1):
    for flat_n in range(flats_per_floor):

        if floor_n == floors:
            flat_name = f"L{floor_n}{flat_n}"
        elif floor_n % 2 == 0:
            flat_name = f"L{floor_n}{flat_n}"
        elif floor_n % 2 != 0:
            flat_name = f"L{floor_n}{flat_n}"

        print(flat_name, end=" ")

    print()