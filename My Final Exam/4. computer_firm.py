number_of_computers = int(input())

total_rating = 0

total_computer_sold = 0

for num in range(number_of_computers):
    possible_sales_and_rating = int(input())

    rating = possible_sales_and_rating % 10

    possible_sales = (possible_sales_and_rating - (possible_sales_and_rating % 10)) / 10

    computers_sold = 0

    if rating == 2:
        computers_sold = 0 * possible_sales
    elif rating == 3:
        computers_sold = 0.5 * possible_sales
    elif rating == 4:
        computers_sold = 0.7 * possible_sales
    elif rating == 5:
        computers_sold = 0.85 * possible_sales
    elif rating == 6:
        computers_sold = 1 * possible_sales

    total_computer_sold += computers_sold

    total_rating += rating

average_rating = total_rating / number_of_computers

print(f"{total_computer_sold:.2f}")
print(f"{average_rating:.2f}")