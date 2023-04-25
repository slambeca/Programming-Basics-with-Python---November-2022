start_number = int(input())
end_number = int(input())

for a in range(start_number, end_number + 1):
    for b in range(start_number, end_number + 1):
        for c in range(start_number, end_number + 1):
            for d in range(start_number, end_number + 1):
                if a % 2 == 0 and d % 2 != 0 and a > d and (b + c) % 2 == 0:
                    print(f"{a}{b}{c}{d}", end=" ")
                if a % 2 != 0 and d % 2 == 0 and a > d and (b + c) % 2 == 0:
                    print(f"{a}{b}{c}{d}", end=" ")