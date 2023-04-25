months = int(input())

electricity_bill = 0
water_bill = 0
internet_bill = 0
others_bill = 0

average_bill = 0

for _ in range(1, months + 1):
    current_electricity_bill = float(input())
    electricity_bill += current_electricity_bill
    current_water_bill = 20
    water_bill += current_water_bill
    current_internet_bill = 15
    internet_bill += current_internet_bill
    others_bill += (current_electricity_bill + current_water_bill + current_internet_bill) * 1.2

average_bill = (electricity_bill + water_bill + internet_bill + others_bill) / months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {others_bill:.2f} lv")
print(f"Average: {average_bill:.2f} lv")