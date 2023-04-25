temperature = float(input())

if 35.00 >= temperature >= 26.00:
    print("Hot")
elif 25.9 >= temperature >= 20.1:
    print("Warm")
elif 20.00 >= temperature >= 15.00:
    print("Mild")
elif 14.9 >= temperature >= 12.00:
    print("Cool")
elif 11.9 >= temperature >= 5:
    print("Cold")
else:
    print("unknown")