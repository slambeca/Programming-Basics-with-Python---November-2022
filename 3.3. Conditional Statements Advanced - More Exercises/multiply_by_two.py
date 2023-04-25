number = float(input())

while number >= 0:
    number_by_two = number * 2
    print(f"Result: {number_by_two:.2f}")
    number = float(input())
else:
    print("Negative number!")