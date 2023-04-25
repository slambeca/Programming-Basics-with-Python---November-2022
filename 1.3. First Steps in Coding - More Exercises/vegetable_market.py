price_kg_vegetables = float(input())
price_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

revenue_vegetables = price_kg_vegetables * total_kg_vegetables
revenue_fruits = price_kg_fruits * total_kg_fruits
total_euro = (revenue_fruits + revenue_vegetables) / 1.94

print(f"{total_euro:.2f}")