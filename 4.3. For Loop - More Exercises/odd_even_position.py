import sys
number = int(input())

odd_sum = float(0)
odd_min = float(sys.maxsize)
odd_max = float(-sys.maxsize)
even_sum = float(0)
even_min = float(sys.maxsize)
even_max = float(-sys.maxsize)

for i in range(1, number + 1):
    num = float(input())
    if i % 2 != 0:
        odd_sum += num
        if num > odd_max:
            odd_max = num
        if num < odd_min:
            odd_min = num
    elif i % 2 == 0:
        even_sum += num
        if num > even_max:
            even_max = num
        if num < even_min:
            even_min = num

print(f"OddSum={odd_sum:.2f},")
if odd_min != 9223372036854775808.00:
    print(f"OddMin={odd_min:.2f},")
else:
    print("OddMin=No,")

if odd_max != -9223372036854775808.00:
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMax=No,")

print(f"EvenSum={even_sum:.2f},")

if even_min != 9223372036854775808.00:
    print(f"EvenMin={even_min:.2f},")
else:
    print("EvenMin=No,")

if even_max != -9223372036854775808.00:
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMax=No")