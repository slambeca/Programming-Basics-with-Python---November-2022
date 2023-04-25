type_fuel = input() # Gas, Gasoline, Diesel
fuel_lts = float(input())
club_card = input() # Yes or No

paid_for_fuel = 0

if club_card == "Yes":
    if type_fuel == "Gas":
        paid_for_fuel = (0.93 - 0.08) * fuel_lts
    elif type_fuel == "Gasoline":
        paid_for_fuel = (2.22 - 0.18) * fuel_lts
    else:
        paid_for_fuel = (2.33 - 0.12) * fuel_lts
else:
    if type_fuel == "Gas":
        paid_for_fuel = 0.93 * fuel_lts
    elif type_fuel == "Gasoline":
        paid_for_fuel = 2.22 * fuel_lts
    else:
        paid_for_fuel = 2.33 * fuel_lts

if 20 <= fuel_lts <= 25:
    paid_for_fuel = paid_for_fuel * 0.92
elif fuel_lts > 25:
    paid_for_fuel = paid_for_fuel * 0.9
else:
    paid_for_fuel = paid_for_fuel

print(f"{paid_for_fuel:.2f} lv.")