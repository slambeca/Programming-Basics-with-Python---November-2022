flour_price_kg = float(input())
flour_kgs = float(input())
sugar_kgs = float(input())
egg_shells = int(input())
yeast_packages = int(input())

sugar_price = flour_price_kg * 0.75
eggs_price = flour_price_kg * 1.1
yeast_price = sugar_price * 0.2

spending_flour = flour_kgs * flour_price_kg
spending_sugar = sugar_kgs * sugar_price
spending_eggs = egg_shells * eggs_price
spending_yeast = yeast_packages * yeast_price

total_sum = spending_sugar + spending_yeast + spending_eggs + spending_flour

print(f"{total_sum:.2f}")