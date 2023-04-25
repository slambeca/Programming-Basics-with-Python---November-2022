numbers = int(input())

total_sum = 0

average = 0

for x in range(numbers):
    number = int(input())

    total_sum += number

    average = total_sum / numbers

print(f"{average:.2f}")