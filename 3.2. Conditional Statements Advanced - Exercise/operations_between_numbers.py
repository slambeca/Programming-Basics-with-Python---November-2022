first_num = int(input())
second_num = int(input())
operator = input()

result = 0
even_or_odd = None

if operator == "+":
    result = first_num + second_num
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_num} {operator} {second_num} = {result} - {even_or_odd}")
elif operator == "-":
    result = first_num - second_num
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_num} {operator} {second_num} = {result} - {even_or_odd}")
elif operator == "*":
    result = first_num * second_num
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_num} {operator} {second_num} = {result} - {even_or_odd}")
elif operator == "/":
    if second_num != 0:
        result = first_num / second_num
        print(f"{first_num} / {second_num} = {result:.2f}")
    else:
        print(f"Cannot divide {first_num} by zero")
elif operator == "%":
    if second_num != 0:
        result = first_num % second_num
        print(f"{first_num} % {second_num} = {result}")
    else:
        print(f"Cannot divide {first_num} by zero")