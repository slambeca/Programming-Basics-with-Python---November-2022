budget = float(input())
season = input()

price = None
location = None
place_of_stay = None

if budget <= 1000:
    place_of_stay = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
if 1000 < budget <= 3000:
    place_of_stay = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    place_of_stay = "Hotel"
    price = budget * 0.9
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} - {place_of_stay} - {price:.2f}")