computer_number = int(input())

avg_rating = 0
sales_count = 0
rating_count = 0

for i in range(computer_number):
    sales_rating = int(input())

    rating = sales_rating % 10
    possible_sales = sales_rating // 10

    if rating == 2:
        sales_made = 0
        sales_count += sales_made
        rating_count += rating
    elif rating == 3:
        sales_made = 0.5*possible_sales
        sales_count += sales_made
        rating_count += rating
    elif rating == 4:
        sales_made = 0.7*possible_sales
        sales_count += sales_made
        rating_count += rating
    elif rating == 5:
        sales_made = 0.85*possible_sales
        sales_count += sales_made
        rating_count += rating
    elif rating == 6:
        sales_made = possible_sales
        sales_count += sales_made
        rating_count += rating

    i += 1

avg_rating = rating_count / computer_number

print(f"{sales_count:.2f}")
print(f"{avg_rating:.2f}")