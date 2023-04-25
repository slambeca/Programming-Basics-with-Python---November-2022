voucher = int(input())

money_left = voucher

price = 0
tickets = 0
other_products = 0

input_line = input()

while input_line != "End":
    product = input_line

    if len(product) > 8:
        price = ord(product[0]) + ord(product[1])
        if money_left < price:
            break
        tickets += 1
    elif len(product) <= 8:
        price = ord(product[0])
        if money_left < price:
            break
        other_products += 1

    money_left -= price

    input_line = input()

print(f"{tickets}")
print(f"{other_products}")