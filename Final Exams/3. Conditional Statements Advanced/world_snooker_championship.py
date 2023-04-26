championship_stage = input()
type_ticket = input()
number_of_tickets = int(input())
trophy_pic = input()

price = None
trophy_pic_price = 40
discount = None

if type_ticket == "Standard":
    if championship_stage == "Quarter final":
        price = 55.50
    elif championship_stage == "Semi final":
        price = 75.88
    elif championship_stage == "Final":
        price = 110.10
elif type_ticket == "Premium":
    if championship_stage == "Quarter final":
        price = 105.20
    elif championship_stage == "Semi final":
        price = 125.22
    elif championship_stage == "Final":
        price = 160.66
elif type_ticket == "VIP":
    if championship_stage == "Quarter final":
        price = 118.90
    elif championship_stage == "Semi final":
        price = 300.40
    elif championship_stage == "Final":
        price = 400.00

total_price = price * number_of_tickets

if 2500 < total_price <= 4000:
    discount = 0.1
elif total_price > 4000:
    discount = 0.25
    trophy_pic_price = 0
else:
    discount = 0

final_price = total_price - (total_price * discount)

if trophy_pic == "N":
    trophy_pic_price = 0
elif trophy_pic == "Y":
    trophy_pic_price = trophy_pic_price * number_of_tickets
elif trophy_pic == "Y" and total_price > 400:
    trophy_pic_price = 0

final_price = final_price + trophy_pic_price
print(f"{final_price:.2f}")