rolls_packing_paper = int(input())
rolls_cloth = int(input())
liters_of_glue = float(input())
discount_percentage = int(input())

price_packing_paper = 5.80
price_cloth = 7.20
price_glue = 1.20

total_price_package_paper = rolls_packing_paper * price_packing_paper
total_price_cloth = rolls_cloth * price_cloth
total_price_glue = liters_of_glue * price_glue

total_price_all = total_price_package_paper + total_price_cloth + total_price_glue

discounted_price = (total_price_all * (100 - discount_percentage)) / 100

print(f"{discounted_price:.3f}")