tax_for_luggage_over_20_kg = float(input())
luggage_weight_kg = float(input())
days_left_to_trip = int(input())
luggage_number = int(input())

tax_for_luggage = 0

if luggage_weight_kg < 10:  # up until 10
    tax_for_luggage = tax_for_luggage_over_20_kg / 5
elif 10 <= luggage_weight_kg <= 20:     # between 10 and 20
    tax_for_luggage = tax_for_luggage_over_20_kg / 2
elif luggage_weight_kg > 20:
    tax_for_luggage = tax_for_luggage_over_20_kg

if days_left_to_trip < 7:
    tax_for_luggage *= 1.4
elif 7 <= days_left_to_trip <= 30:
    tax_for_luggage *= 1.15
elif days_left_to_trip > 30:
    tax_for_luggage *= 1.1

total_paid = luggage_number * tax_for_luggage

print(f"The total price of bags is: {total_paid:.2f} lv.")