country = input()
item = input()

result_one = None
result_two = None

if item == "ribbon":
    if country == "Russia":
        result_one = 9.100
        result_two = 9.400
    elif country == "Bulgaria":
        result_one = 9.600
        result_two = 9.400
    elif country == "Italy":
        result_one = 9.200
        result_two = 9.500
elif item == "hoop":
    if country == "Russia":
        result_one = 9.300
        result_two = 9.800
    elif country == "Bulgaria":
        result_one = 9.550
        result_two = 9.750
    elif country == "Italy":
        result_one = 9.450
        result_two = 9.350
elif item == "rope":
    if country == "Russia":
        result_one = 9.600
        result_two = 9.000
    elif country == "Bulgaria":
        result_one = 9.500
        result_two = 9.400
    elif country == "Italy":
        result_one = 9.700
        result_two = 9.150

final_score = result_one + result_two
max_score = 20 - final_score
percent_to_max_score = (max_score / 20) * 100

print(f"The team of {country} get {final_score:.3f} on {item}.")
print(f"{percent_to_max_score:.2f}%")