nylon_sq_mt = int(input())
paint_lt = int(input())
thinner_lt = int(input())
work_hours = int(input())

nylon_price = (nylon_sq_mt + 2) * 1.5
paint_price = ((paint_lt * 1.1) * 14.50)
thinner_price = thinner_lt * 5
bag_price = 0.4

sum_materials = nylon_price + paint_price + thinner_price + bag_price

# short code
# sum_materials = (nylon_price + 2) * 1.5 + (paint_lt + 0.10 * paint_lt) * 14.50 + thinner_lt * 5.0 + 0.4
# one line instead of four

price_work_hour = (sum_materials * 0.3) * work_hours

total_sum = sum_materials + price_work_hour

print(total_sum)