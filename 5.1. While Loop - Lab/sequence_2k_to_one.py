number = int(input())

counter = 1     # we start with 1, because 0 * 1, 0 * 2, 0 * 3 will be equal to 0

while counter <= number:
    print(counter)
    counter = counter * 2 + 1