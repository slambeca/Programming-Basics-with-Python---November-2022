square_meters_for_landscaping = float(input())

price_for_landscaping_for_square_meter = square_meters_for_landscaping * 7.61
discount = price_for_landscaping_for_square_meter * 0.18

print(f"The final price is: {price_for_landscaping_for_square_meter - discount} lv.")
print(f"The discount is: {discount} lv.")