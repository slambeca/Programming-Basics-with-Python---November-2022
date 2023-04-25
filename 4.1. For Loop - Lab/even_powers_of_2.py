number = int(input())

for num in range(number + 1):
    if num % 2 == 0:    # for the first iteration where num = 0, 2 ** 0 (num) = 1
        print(2 ** num)