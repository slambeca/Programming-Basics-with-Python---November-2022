number_of_clients = int(input())

total_sum_for_all_clients = 0

for count in range(number_of_clients):
    current_sum = 0
    product_counter = 0

    while True:
        product = input()

        if product == "Finish":
            break

        product_counter += 1

        if product == "basket":
            current_sum += 1.50
        elif product == "wreath":
            current_sum += 3.80
        elif product == "chocolate bunny":
            current_sum += 7

    if product_counter % 2 == 0:
        current_sum *= 0.8

    total_sum_for_all_clients += current_sum
    print(f"You purchased {product_counter} items for {current_sum:.2f} leva.")

total_sum_for_all_clients /= number_of_clients
print(f"Average bill per client is: {total_sum_for_all_clients:.2f}")