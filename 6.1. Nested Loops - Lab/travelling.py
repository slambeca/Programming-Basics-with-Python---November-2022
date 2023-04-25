destination = input()

savings = 0

while destination != "End":
    budget = float(input())
    while budget > savings:
        saved_money = float(input())
        savings += saved_money
        if savings >= budget:
            print(f"Going to {destination}!")
            savings = 0
            break

    destination = input()

# Variant 2
# while True:
#     destination = input()
#
#     if destination == "End":
#         break
#
#     budget = float(input())
#     total_sum = 0
#
#     while True:
#         saved_money = float(input())
#         total_sum += saved_money
#         if total_sum >= budget:
#             print(f"Going to {destination}!")
#             break

# Variant 3
# input_line = input()
#
# while input_line != "End":
#     destination = input_line
#     money_needed = float(input())
#
#     money_saved = 0
#
#     while money_saved < money_needed:
#         saved_money = float(input())
#         money_saved += saved_money
#
#         if money_saved >= money_needed:
#             print(f"Going to {destination}!")
#
#     input_line = input()