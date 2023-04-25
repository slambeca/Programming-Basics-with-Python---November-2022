annual_tax = int(input())

sneakers_price = (annual_tax * 0.6)     # or annual_tax - (annual_tax * 0.40)
jersey_price = (sneakers_price * 0.8)   # or sneakers_price - (sneakers_price * 0.20)
ball_price = (jersey_price * 0.25)      # or jersey_price / 4
acc_price = (ball_price * 0.2)          # or ball_price / 5

total_price = annual_tax + sneakers_price + jersey_price + ball_price + acc_price

print(f"{total_price:.2f}")