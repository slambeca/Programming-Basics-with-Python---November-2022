percent_fat = int(input())
percent_proteins = int(input())
percent_carbs = int(input())
total_calories = int(input())
percent_water = int(input())

total_grams_fat = ((total_calories * percent_fat) / 9) / 100
total_grams_proteins = ((total_calories * percent_proteins) / 4) / 100
total_grams_carbs = ((total_calories * percent_carbs) / 4) / 100

total_grams_food = total_grams_fat + total_grams_proteins + total_grams_carbs
calories_per_one_gram = total_calories / total_grams_food

food_without_water = (calories_per_one_gram * abs(percent_water - 100)) / 100

print(f"{food_without_water:.4f}")