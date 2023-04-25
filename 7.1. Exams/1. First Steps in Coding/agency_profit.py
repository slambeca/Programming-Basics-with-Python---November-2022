agency_name = str(input())
number_of_tickets_adults = int(input())
number_of_tickets_children = int(input())
net_price_adult_ticket = float(input())
service_tax = float(input())

net_price_children_ticket = net_price_adult_ticket * 0.3
final_price_adult_ticket = net_price_adult_ticket + service_tax
final_price_children_ticket = net_price_children_ticket + service_tax

final_sum_tickets = (number_of_tickets_children * final_price_children_ticket) + \
                    (number_of_tickets_adults * final_price_adult_ticket)

revenue = final_sum_tickets / 5
print(f"The profit of your agency from {agency_name} tickets is {revenue:.2f} lv.")