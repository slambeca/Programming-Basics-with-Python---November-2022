from math import ceil, floor

tennis_racket_price = float(input())
tennis_racket_number = int(input())
pair_of_sneakers = int(input())

sum_paid_for_tennis_rackets = (tennis_racket_number * tennis_racket_price)
price_for_pair_of_sneakers = (tennis_racket_price / 6)
total_price_for_sneakers = price_for_pair_of_sneakers * pair_of_sneakers

other_equipment_price = (sum_paid_for_tennis_rackets + total_price_for_sneakers) / 5

total_sum = sum_paid_for_tennis_rackets + total_price_for_sneakers + other_equipment_price
total_sum_Djokovic = total_sum / 8
total_sum_sponsors = total_sum * 7 / 8

print(f"Price to be paid by Djokovic {floor(total_sum_Djokovic)}")
print(f"Price to be paid by sponsors {ceil(total_sum_sponsors)}")