count_men = int(input())
count_women = int(input())
maximum_count_tables = int(input())

combinations = 0

no_more_tables = False

for man in range(1, count_men + 1):
    for woman in range(1, count_women + 1):
        print(f"({man} <-> {woman})", end=" ")

        combinations += 1

        if combinations == maximum_count_tables:
            no_more_tables = True
            break
    if no_more_tables:
        break