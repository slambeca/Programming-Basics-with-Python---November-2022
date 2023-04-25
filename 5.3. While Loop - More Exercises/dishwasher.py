bottles_of_detergent = int(input())

detergent_quantity = bottles_of_detergent * 750

reloading = 0

plates_washed = 0
pots_washed = 0

used_detergent = 0

input_line = input()

while input_line != "End":
    reloading += 1
    count_dishes = int(input_line)

    if reloading % 3 == 0:
        used_detergent = count_dishes * 15
        detergent_quantity -= used_detergent
        pots_washed += count_dishes
    else:
        used_detergent = count_dishes * 5
        detergent_quantity -= used_detergent
        plates_washed += count_dishes

    if detergent_quantity < 0:
        print(f"Not enough detergent, {abs(detergent_quantity)} ml. more necessary!")
        break

    input_line = input()

else:
    print(f"Detergent was enough!")
    print(f"{plates_washed} dishes and {pots_washed} pots were washed.")
    print(f"Leftover detergent {detergent_quantity} ml.")