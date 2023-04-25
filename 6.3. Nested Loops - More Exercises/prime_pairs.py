start_first_pair = int(input())
start_second_pair = int(input())
diff_for_end_first_pair = int(input())
diff_for_end_second_pair = int(input())

end_first_pair = start_first_pair + diff_for_end_first_pair
end_second_pair = start_second_pair + diff_for_end_second_pair

for x in range(start_first_pair, end_first_pair + 1):
    is_prime = True
    for a in range(2, x):
        if x % a == 0:
            is_prime = False

    for y in range(start_second_pair, end_second_pair + 1):
        is_prime_two = True
        for b in range(2, y):
            if y % b == 0:
                is_prime_two = False

        if is_prime and is_prime_two:
            print(f"{x}{y}", end="\n")