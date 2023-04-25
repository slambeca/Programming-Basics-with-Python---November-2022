food_bought_kgs = int(input())

food_bought_grams = food_bought_kgs * 1000

input_line = input()

total_food_eaten = 0

food_is_not_sufficient = False

while input_line != "Adopted":
    daily_food_eaten = int(input_line)

    food_bought_grams -= daily_food_eaten
    total_food_eaten += daily_food_eaten

    if food_bought_grams < 0:
        food_is_not_sufficient = True

    input_line = input()

if food_is_not_sufficient:
    print(f"Food is not enough. You need {abs(food_bought_grams)} grams more.")
else:
    print(f"Food is enough! Leftovers: {food_bought_grams} grams.")