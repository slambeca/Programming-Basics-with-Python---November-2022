from math import pi

figure = input()
area = 0 # so that the program doesn`t yell at us if we choose something other than the 4 figures

if figure == "square":
    a = float(input())
    area = a * a
elif figure == "rectangle":
    a, b = float(input()), float(input())
    area = a * b
elif figure == "circle":
    r = float(input())
    area = r ** 2 * pi
elif figure == "triangle":
    a, h = float(input()), float(input())
    area = a * h / 2

print(f"{area:.3f}")