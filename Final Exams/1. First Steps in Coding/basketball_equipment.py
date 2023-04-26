annual_tax = int(input())

sneakers_price = (annual_tax * 0.6)
jersey_price = (sneakers_price * 0.8)
ball_price = (jersey_price * 0.25)
acc_price = (ball_price * 0.2)
total_price = annual_tax + sneakers_price + jersey_price + ball_price + acc_price

print(f"{total_price:.2f}")
