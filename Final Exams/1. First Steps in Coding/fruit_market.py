strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price / 2
sum_price_raspberries = raspberries_kg * raspberries_price
oranges_price = (raspberries_price * 0.6) * oranges_kg
bananas_price = (raspberries_price / 5) * bananas_kg

sum_price_strawberries = strawberries_price * strawberries_kg

total_sum = sum_price_raspberries + oranges_price + bananas_price + sum_price_strawberries
formatted_total_sum = "{:.2f}".format(total_sum)

print(formatted_total_sum)