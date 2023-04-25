first_number = int(input())
second_number = int(input())
magic_number = int(input())

combination_counter = 0

magic_number_condition = False

for x in range(first_number, second_number + 1):
    for y in range(first_number, second_number + 1):
        combination_counter += 1   # we are looking for combinations of numbers and each iteration should be considered

        if x + y == magic_number:
            print(f"Combination N:{combination_counter} ({x} + {y} = {magic_number})")
            magic_number_condition = True
            break   # break out of the inner loop

    if magic_number_condition:
        break   # break out of the outer loop

if not magic_number_condition:
    print(f"{combination_counter} combinations - neither equals {magic_number}")