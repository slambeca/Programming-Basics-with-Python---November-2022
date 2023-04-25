wanted_revenue = int(input())

input_line = input()

paid_by_cash = 0
paid_by_credit_card = 0

count_paid_by_cash = 0
count_paid_by_credit_card = 0

total_sum = 0

iteration = 0

while input_line != "End":
    iteration += 1
    transaction = int(input_line)

    if iteration % 2 != 0:
        if transaction > 100:
            print(f"Error in transaction!")
        else:
            paid_by_cash += transaction
            total_sum += transaction
            count_paid_by_cash += 1
            print(f"Product sold!")

    else:
        if transaction < 10:
            print(f"Error in transaction!")
        else:
            paid_by_credit_card += transaction
            total_sum += transaction
            count_paid_by_credit_card += 1
            print(f"Product sold!")

    if total_sum >= wanted_revenue:
        print(f"Average CS: {paid_by_cash / count_paid_by_cash:.2f}")
        print(f"Average CC: {paid_by_credit_card / count_paid_by_credit_card:.2f}")
        break

    input_line = input()

else:
    print(f"Failed to collect required money for charity.")