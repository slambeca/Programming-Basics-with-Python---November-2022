from math import ceil, floor

days = int(input())
food_left_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gram = float(input())

dog_food_needed = days * dog_food_kg
cat_food_needed = days * cat_food_kg
turtle_food_needed = days * turtle_food_gram / 1000
total_food_needed = dog_food_needed + cat_food_needed + turtle_food_needed
food_left_at_end = food_left_kg - total_food_needed

if total_food_needed <= food_left_kg:
    print(f"{floor(food_left_at_end)} kilos of food left.")
else:
    print(f"{ceil(total_food_needed - food_left_kg)} more kilos of food are needed.")