screening_type = input()
rows = int(input())
columns = int(input())

cinema_capacity = rows * columns

profit = 0

if screening_type == "Premiere":
    profit = cinema_capacity * 12
elif screening_type == "Normal":
    profit = cinema_capacity * 7.5
else:
    profit = cinema_capacity * 5

print(f"{profit:.2f} leva")