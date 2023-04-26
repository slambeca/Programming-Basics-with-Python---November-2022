capacity = float(input())

count_suitcases = 0
iteration = 0
available_space = capacity

input_line = input()

no_more_space = False

while input_line != "End":
    suitcase_volume = float(input_line)
    iteration += 1

    if iteration == 3:
        suitcase_volume *= 1.10

    if suitcase_volume >= available_space:
        no_more_space = True
        break

    available_space -= suitcase_volume
    count_suitcases += 1

    input_line = input()

if no_more_space:
    print(f"No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {count_suitcases} suitcases loaded.")