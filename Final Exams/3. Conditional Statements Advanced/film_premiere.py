movie = input()
package = input()
ticket_numbers = int(input())

price = None
discount = None

if package == "Drink":
    if movie == "John Wick":
        price = 12
    elif movie == "Star Wars":
        price = 18
    elif movie == "Jumanji":
        price = 9
elif package == "Popcorn":
    if movie == "John Wick":
        price = 15
    elif movie == "Star Wars":
        price = 25
    elif movie == "Jumanji":
        price = 11
elif package == "Menu":
    if movie == "John Wick":
        price = 19
    elif movie == "Star Wars":
        price = 30
    elif movie == "Jumanji":
        price = 14

total_price = price * ticket_numbers

if movie == "Star Wars" and ticket_numbers >= 4:
    total_price *= 0.7
elif movie == "Jumanji" and ticket_numbers == 2:
    total_price *= 0.85

print(f"Your bill is {total_price:.2f} leva.")