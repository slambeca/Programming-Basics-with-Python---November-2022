number_of_easter_breads = int(input())
number_of_egg_shells = int(input())
cookies_kg = int(input())

price_easter_breads = number_of_easter_breads * 3.2
price_egg_shells = number_of_egg_shells * 4.35
price_cookies = cookies_kg * 5.40
price_egg_paint = number_of_egg_shells * 12 * 0.15

total_sum = price_easter_breads + price_egg_shells + price_cookies + price_egg_paint

print(f"{total_sum:.2f}")