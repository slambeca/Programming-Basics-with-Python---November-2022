initial_eggs = int(input())

command = input()

bought_eggs = 0

while command != "Close":
    eggs_sold = int(input())

    if command == "Buy":
        if initial_eggs < eggs_sold:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {initial_eggs}.")
            break
        bought_eggs += eggs_sold
        initial_eggs -= eggs_sold
    elif command == "Fill":
        initial_eggs += eggs_sold

    command = input()

else:
    print(f"Store is closed!")
    print(f"{bought_eggs} eggs sold.")