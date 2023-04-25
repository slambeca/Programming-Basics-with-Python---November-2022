pen_packages = int(input())
marker_packages = int(input())
cleaning_detergent_liters = int(input())
discount_percentage = int(input())

price_pens = pen_packages * 5.80
price_markers = marker_packages * 7.20
price_cleaning_detergent = cleaning_detergent_liters * 1.20

total_price = price_pens + price_markers + price_cleaning_detergent
final_price = total_price - (total_price * discount_percentage / 100)

print(final_price)