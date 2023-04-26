from math import ceil

easter_breads = int(input())

sugar_needed = 0
flour_needed = 0

sugar_packages_needed = 0
flour_packages_needed = 0

max_sugar_quantity = 0
max_flour_quantity = 0

for _ in range(1, easter_breads + 1):
    sugar_quantity = int(input())
    flour_quantity = int(input())
    sugar_needed += sugar_quantity
    flour_needed += flour_quantity

    if sugar_quantity > max_sugar_quantity:
        max_sugar_quantity = sugar_quantity

    if flour_quantity > max_flour_quantity:
        max_flour_quantity = flour_quantity

flour_packages_needed = ceil(flour_needed / 750)
sugar_packages_needed = ceil(sugar_needed / 950)

print(f"Sugar: {sugar_packages_needed}")
print(f"Flour: {flour_packages_needed}")
print(f"Max used flour is {max_flour_quantity} grams, "
      f"max used sugar is {max_sugar_quantity} grams.")