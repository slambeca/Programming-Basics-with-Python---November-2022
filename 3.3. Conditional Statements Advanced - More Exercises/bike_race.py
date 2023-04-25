young_participants = int(input())
senior_participants = int(input())
trail_type = input()

juniors_price = None
seniors_price = None
total_price = None

if trail_type == "trail":
    juniors_price = 5.50 * young_participants
    seniors_price = 7 * senior_participants
    total_price = juniors_price + seniors_price
elif trail_type == "cross-country":
    juniors_price = 8 * young_participants
    seniors_price = 9.50 * senior_participants
    total_price = juniors_price + seniors_price
    if young_participants + senior_participants >= 50:
        total_price *= 0.75
elif trail_type == "downhill":
    juniors_price = 12.25 * young_participants
    seniors_price = 13.75 * senior_participants
    total_price = juniors_price + seniors_price
elif trail_type == "road":
    juniors_price = 20 * young_participants
    seniors_price = 21.50 * senior_participants
    total_price = juniors_price + seniors_price

spendings = total_price * 0.05

print(f"{total_price - spendings:.2f}")