budget = float(input())
season = input()

destination = None
type_of_vacation = None

money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = budget * 0.3
        type_of_vacation = "Camp"
    elif season == "winter":
        money_spent = budget * 0.7
        type_of_vacation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = budget * 0.4
        type_of_vacation = "Camp"
    elif season == "winter":
        money_spent = budget * 0.8
        type_of_vacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    money_spent = budget * 0.9
    type_of_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {money_spent:.2f}")