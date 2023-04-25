number = int(input())

p1_numbers = 0
p2_numbers = 0
p3_numbers = 0

for _ in range(1, number + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        p1_numbers += 1
    if current_number % 3 == 0:
        p2_numbers += 1
    if current_number % 4 == 0:
        p3_numbers += 1
    else:
        pass

p1_numbers = (p1_numbers / number) * 100
p2_numbers = (p2_numbers / number) * 100
p3_numbers = (p3_numbers / number) * 100

print(f"{p1_numbers:.2f}%")
print(f"{p2_numbers:.2f}%")
print(f"{p3_numbers:.2f}%")