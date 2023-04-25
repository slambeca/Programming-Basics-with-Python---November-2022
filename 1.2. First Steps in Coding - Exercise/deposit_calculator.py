deposited_sum = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())

per_year = deposited_sum * (annual_interest_rate / 100)
per_month = per_year / 12

total_sum = deposited_sum + term_of_the_deposit * per_month

print(total_sum)