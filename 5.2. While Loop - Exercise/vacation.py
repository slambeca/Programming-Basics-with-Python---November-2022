money_for_vacation_needed = float(input())
initial_money = float(input())

total_sum = initial_money

days_counter = 0
spending_days_counter = 0

while total_sum < money_for_vacation_needed:
    if spending_days_counter >= 5:
        break

    action = input()
    amount = float(input())

    days_counter += 1

    if action == "spend":
        total_sum -= amount
        spending_days_counter += 1
        if total_sum < 0:
            total_sum = 0

    elif action == "save":
        total_sum += amount
        spending_days_counter = 0

if spending_days_counter == 5:
    print(f"You can't save the money.")
    print(days_counter)
else:
    print(f"You saved the money for {days_counter} days.")