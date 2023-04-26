contract_term = input()
type_term = input()
internet = input()
months = int(input())

price = 0
total_price = 0
internet_price = 0

if type_term == "Small":
    if contract_term == "one":
        price = 9.98
    elif contract_term == "two":
        price = 8.58
elif type_term == "Middle":
    if contract_term == "one":
        price = 18.99
    elif contract_term == "two":
        price = 17.09
elif type_term == "Large":
    if contract_term == "one":
        price = 25.98
    elif contract_term == "two":
        price = 23.59
elif type_term == "ExtraLarge":
    if contract_term == "one":
        price = 35.99
    elif contract_term == "two":
        price = 31.79

if internet == "yes":
    if price <= 10:
        internet_price = 5.50
    elif price <= 30:
        internet_price = 4.35
    elif price > 30:
        internet_price = 3.85
elif internet == "no":
    internet_price = 0

total_price = (price + internet_price) * months

if contract_term == "two":
    total_price = total_price * 0.9625
else:
    total_price = total_price

print(f"{total_price:.2f} lv.")