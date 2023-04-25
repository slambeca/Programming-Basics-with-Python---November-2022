start_number = int(input())
end_number = int(input())
magic_number = int(input())

combinations = 0

x = 0
y = 0

flag = False

for x in range(start_number, end_number + 1):
    for y in range(start_number, end_number + 1):
        combinations += 1
        if x + y == magic_number:
            flag = True
            break
    if flag:
        break

if flag:
    print(f"Combination N:{combinations} ({x} + {y} = {magic_number})")
else:
    print(f"{combinations} combinations - neither equals {magic_number}")