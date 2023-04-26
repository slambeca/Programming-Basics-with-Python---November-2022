budget = float(input())
needed_fuel_lt = float(input())
day_of_week = input()

paid_for_fuel = needed_fuel_lt * 2.10
paid_for_fuel_and_tour_guide = paid_for_fuel + 100

if day_of_week == "Sunday":
    paid_for_fuel_and_tour_guide = paid_for_fuel_and_tour_guide * 0.8
else:
    paid_for_fuel_and_tour_guide = paid_for_fuel_and_tour_guide * 0.9

if paid_for_fuel_and_tour_guide <= budget:
    print(f"Safari time! Money left: {budget - paid_for_fuel_and_tour_guide:.2f} lv.")
elif paid_for_fuel_and_tour_guide > budget:
    print(f"Not enough money! Money needed: {paid_for_fuel_and_tour_guide - budget:.2f} lv.")