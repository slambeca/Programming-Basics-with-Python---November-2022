movie_name = input()
hall_type = input()
tickets_bought = int(input())

revenue = None
ticket_price = None

if movie_name == "A Star Is Born":
    if hall_type == "normal":
        ticket_price = 7.5
    elif hall_type == "luxury":
        ticket_price = 10.5
    else:
        ticket_price = 13.5
elif movie_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        ticket_price = 7.35
    elif hall_type == "luxury":
        ticket_price = 9.45
    else:
        ticket_price = 12.75
elif movie_name == "Green Book":
    if hall_type == "normal":
        ticket_price = 8.15
    elif hall_type == "luxury":
        ticket_price = 10.25
    else:
        ticket_price = 13.25
else:
    if hall_type == "normal":
        ticket_price = 8.75
    elif hall_type == "luxury":
        ticket_price = 11.55
    else:
        ticket_price = 13.95

revenue = ticket_price * tickets_bought

print(f"{movie_name} -> {revenue:.2f} lv.")