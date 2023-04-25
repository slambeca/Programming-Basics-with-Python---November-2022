budget = float(input())

input_line = input()

count_products = 0

total_sum = 0

while input_line != "Stop":
    product_price = float(input())
    count_products += 1

    if count_products % 3 == 0:
        product_price = product_price / 2

    if budget - product_price < 0:
        print(f"You don't have enough money!")
        print(f"You need {abs(product_price - budget):.2f} leva!")
        break

    budget -= product_price
    total_sum += product_price
    input_line = input()

if input_line == "Stop":
    print(f"You bought {count_products} products for {total_sum:.2f} leva.")