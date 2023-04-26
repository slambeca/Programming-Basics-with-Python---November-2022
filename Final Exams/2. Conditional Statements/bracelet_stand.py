day_allowing = float(input())
revenue_each_day = float(input())
total_money_spent = float(input())
present_price = float(input())

days = 5

money_saved_from_allowance = days * day_allowing
total_revenue = days * revenue_each_day
total_money_saved = money_saved_from_allowance + total_revenue

money_after_spending = total_money_saved - total_money_spent

if money_after_spending >= present_price:
    print(f"Profit: {money_after_spending:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {present_price - money_after_spending:.2f} BGN.")