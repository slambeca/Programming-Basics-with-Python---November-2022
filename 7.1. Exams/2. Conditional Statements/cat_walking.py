minutes_walking = int(input())
number_of_walks = int(input())
calories_eaten = int(input())

total_minutes_walking = minutes_walking * number_of_walks
calories_burnt = total_minutes_walking * 5
half_of_calories_eaten = calories_eaten / 2

if calories_burnt >= half_of_calories_eaten:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.")