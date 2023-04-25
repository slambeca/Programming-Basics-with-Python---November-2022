budget = float(input())

salary = 0

input_line = input()

no_more_budget = False

while input_line != "ACTION":
    actor_name = input_line

    if len(actor_name) > 15:
        salary = budget * 0.20
    else:
        salary = float(input())

    budget -= salary

    if budget <= 0:
        no_more_budget = True
        break

    input_line = input()

if no_more_budget:
    print(f"We need {abs(budget):.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")