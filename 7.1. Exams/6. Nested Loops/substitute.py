k = int(input())
l = int(input())
m = int(input())
n = int(input())

first_of_number = 0
second_of_number = 0

counter_of_substitutions = 0
limited_substitutions = False

first_number_correct = False
second_number_correct = False

for first_number in range(k, 9):
    if first_number % 2 == 0:
        for second_number in range(9, l-1, -1):
            if second_number % 2 != 0:
                first_of_number = str(f"{first_number}{second_number}")

                for third_number in range(m, 9):
                    if limited_substitutions:
                        break
                    if third_number % 2 == 0:
                        for fourth_number in range(9, n - 1, -1):
                            if fourth_number % 2 != 0:
                                second_of_number = str(f"{third_number}{fourth_number}")
                                if second_of_number != first_of_number:
                                    print(f"{first_of_number} - {second_of_number}")
                                    counter_of_substitutions += 1
                                    if counter_of_substitutions >= 6:
                                        limited_substitutions = True
                                        break
                                else:
                                    print("Cannot change the same player.")