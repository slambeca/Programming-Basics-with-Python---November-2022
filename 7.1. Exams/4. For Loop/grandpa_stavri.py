days = int(input())

total_liters = 0
average_degree = 0

for _ in range(1, days + 1):
    rakia_quantity = float(input())
    degree_of_rakia = float(input())
    total_liters += rakia_quantity
    average_degree += rakia_quantity * degree_of_rakia

average_degree /= total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degree:.2f}")

if average_degree < 38:
    print(f"Not good, you should baking!")
elif average_degree <= 42:
    print(f"Super!")
else:
    print(f"Dilution with distilled water!")