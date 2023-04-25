people = int(input())

back_training = 0
chest_training = 0
legs_training = 0
abs_training = 0

protein_shakes_sold = 0
protein_bars_sold = 0

percent_working_out = 0
percent_proteins = 0

for _ in range(1, people + 1):
    current_activity = input()
    if current_activity == "Back":
        back_training += 1
        percent_working_out += 1
    elif current_activity == "Chest":
        chest_training += 1
        percent_working_out += 1
    elif current_activity == "Legs":
        legs_training += 1
        percent_working_out += 1
    elif current_activity == "Abs":
        abs_training += 1
        percent_working_out += 1
    elif current_activity == "Protein shake":
        protein_shakes_sold += 1
        percent_proteins += 1
    elif current_activity == "Protein bar":
        protein_bars_sold += 1
        percent_proteins += 1

percent_working_out = (percent_working_out / people) * 100
percent_proteins = (percent_proteins / people) * 100

print(f"{back_training} - back")
print(f"{chest_training} - chest")
print(f"{legs_training} - legs")
print(f"{abs_training} - abs")
print(f"{protein_shakes_sold} - protein shake")
print(f"{protein_bars_sold} - protein bar")
print(f"{percent_working_out:.2f}% - work out")
print(f"{percent_proteins:.2f}% - protein")