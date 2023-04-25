number = int(input())

p1_numbers = 0
p2_numbers = 0
p3_numbers = 0
p4_numbers = 0
p5_numbers = 0

for _ in range(1, number + 1):
    current_number = int(input())
    if current_number < 200:
        p1_numbers += 1
    elif 200 <= current_number <= 399:
        p2_numbers += 1
    elif 400 <= current_number <= 599:
        p3_numbers += 1
    elif 600 <= current_number <= 799:
        p4_numbers += 1
    elif current_number >= 800:
        p5_numbers += 1

percent_p1 = (p1_numbers / number) * 100
percent_p2 = (p2_numbers / number) * 100
percent_p3 = (p3_numbers / number) * 100
percent_p4 = (p4_numbers / number) * 100
percent_p5 = (p5_numbers / number) * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")