budget = float(input())
gpu_number = int(input())
cpu_number = int(input())
ram_number = int(input())

gpu_sum = gpu_number * 250
cpu_price = 0.35 * gpu_sum
cpu_sum = cpu_number * cpu_price
ram_price = 0.1 * gpu_sum
ram_sum = ram_number * ram_price

total_sum = gpu_sum + cpu_sum + ram_sum

if gpu_number > cpu_number:
    total_sum = total_sum * 0.85

if total_sum <= budget:
    print(f"You have {budget - total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")