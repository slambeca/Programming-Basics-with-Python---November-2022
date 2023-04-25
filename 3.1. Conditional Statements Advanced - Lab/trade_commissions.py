city = input()
sales = float(input())

commission = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 5
    elif 500 < sales <= 1000:
        commission = 7
    elif 1000 < sales <= 10000:
        commission = 8
    elif sales > 10000:
        commission = 12
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5
    elif 500 < sales <= 1000:
        commission = 7.5
    elif 1000 < sales <= 10000:
        commission = 10
    elif sales > 10000:
        commission = 13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5
    elif 500 < sales <= 1000:
        commission = 8
    elif 1000 < sales <= 10000:
        commission = 12
    elif sales > 10000:
        commission = 14.5

if commission == 0:
    print("error")
else:
    print(f"{sales * commission / 100:.2f}")