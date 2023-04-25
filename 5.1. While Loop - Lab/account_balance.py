balance = 0

while True:
    deposits = input()

    if deposits == "NoMoreMoney":
        break

    deposits = float(deposits)

    if deposits >= 0:
        print(f"Increase: {deposits:.2f}")
        balance += float(deposits)
    else:
        print("Invalid operation!")
        break

print(f"Total: {balance:.2f}")