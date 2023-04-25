movie_name = str(input())
duration_days = int(input())
number_tickets = int(input())
ticket_price = float(input())
cinema_percentage = int(input())

price_tickets_day = number_tickets * ticket_price
total_revenue = duration_days * price_tickets_day
cinema_revenue = total_revenue * cinema_percentage / 100

profit = total_revenue - cinema_revenue

print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")