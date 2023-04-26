input_line = input()

total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while input_line != "Finish":
    movie_name = input_line
    capacity = int(input())

    current_count_tickets = 0

    command_line = input()

    while command_line != "End":
        type_ticket = command_line
        current_count_tickets += 1
        total_tickets += 1

        if type_ticket == "student":
            student_tickets += 1
        elif type_ticket == "standard":
            standard_tickets += 1
        elif type_ticket == "kid":
            kids_tickets += 1

        if current_count_tickets == capacity:
            break

        command_line = input()

    percent_from_capacity = current_count_tickets / capacity * 100
    print(f"{movie_name} - {percent_from_capacity:.2f}% full.")

    input_line = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / total_tickets * 100:.2f}% kids tickets.")