time_for_filming = int(input())
number_scenes = int(input())
time_for_a_scene = int(input())

time_for_preparation = time_for_filming * 0.15
total_time_for_all_scenes = number_scenes * time_for_a_scene
sum_time = time_for_preparation + total_time_for_all_scenes

if sum_time >= time_for_filming:
    print(f"Time is up! To complete the movie you need {round(sum_time - time_for_filming)} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {round(time_for_filming - sum_time)} minutes left!")