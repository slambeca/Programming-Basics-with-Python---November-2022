days = int(input())
total_food = float(int(input()))

food_eaten = 0
eaten_biscuits = 0

eaten_by_dog = 0
eaten_by_cat = 0

for day in range(1, days + 1):
    dog_food_eaten = int(input())
    eaten_by_dog += dog_food_eaten
    cat_food_eaten = int(input())
    eaten_by_cat += cat_food_eaten

    food_eaten += (dog_food_eaten + cat_food_eaten)

    if day % 3 == 0:
        eaten_biscuits += (dog_food_eaten + cat_food_eaten) * 0.1

percent_food_eaten = (food_eaten / total_food) * 100

print(f"Total eaten biscuits: {round(eaten_biscuits)}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{(eaten_by_dog / food_eaten) * 100:.2f}% eaten from the dog.")
print(f"{(eaten_by_cat / food_eaten) * 100:.2f}% eaten from the cat.")