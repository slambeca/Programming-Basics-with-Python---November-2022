daily_goal = int(input())

money_count = 0

while money_count < daily_goal:
    command = input()

    if command != "closed":
        type_of_procedure = input()

        if command == "haircut":
            if type_of_procedure == "mens":
                money_count += 15
            if type_of_procedure == "ladies":
                money_count += 20
            if type_of_procedure == "kids":
                money_count += 10

        if command == "color":
            if type_of_procedure == "touch up":
                money_count += 20
            if type_of_procedure == "full color":
                money_count += 30
    if command == "closed":
        break

if money_count >= daily_goal:
    print("You have reached your target for the day!")
else:
    diff = abs(daily_goal - money_count)
    print(f"Target not reached! You need {diff}lv. more.")

print(f"Earned money: {money_count}lv.")