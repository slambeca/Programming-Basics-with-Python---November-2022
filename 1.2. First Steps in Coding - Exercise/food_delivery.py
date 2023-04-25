chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chicken_menu_price = chicken_menu * 10.35
fish_menu_price = fish_menu * 12.40
vegetarian_menu_price = vegetarian_menu * 8.15

dessert_price = (chicken_menu_price + fish_menu_price + vegetarian_menu_price) * 0.2

delivery_price = 2.50

total_sum = chicken_menu_price + fish_menu_price + vegetarian_menu_price + dessert_price + delivery_price

print(total_sum)