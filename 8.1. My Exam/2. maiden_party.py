price_of_the_maiden_party = float(input())
number_of_love_letters = int(input())
number_of_wax_roses = int(input())
number_of_keychains = int(input())
number_of_caricatures = int(input())
number_of_lucky_surprises = int(input())

total_sum = 0

count_products_sold = 0

price_love_letter = 0.60
price_was_rose = 7.20
price_keychain = 3.60
price_caricature = 18.20
price_lucky_surprise = 22

revenue_from_sales = number_of_love_letters * price_love_letter + number_of_wax_roses * price_was_rose + \
                     number_of_keychains * price_keychain + number_of_caricatures * price_caricature + \
                     number_of_lucky_surprises * price_lucky_surprise

total_products_sold = number_of_lucky_surprises + number_of_caricatures + number_of_love_letters + number_of_keychains + \
                      number_of_wax_roses

if total_products_sold >= 25:
    revenue_from_sales *= 0.65

final_revenue = revenue_from_sales * 0.9

diff = abs(final_revenue - price_of_the_maiden_party)

if final_revenue >= price_of_the_maiden_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")