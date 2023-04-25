number = int(input())

current_num = 1

flag = False

for row in range(1, number + 1):
    for col in range(1, row + 1):
        if current_num > number:
            flag = True
            break
        print(current_num, end=" ")
        current_num += 1
    if flag:
        break
    print()