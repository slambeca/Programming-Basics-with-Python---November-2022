number_of_bitcoins = int(input())
number_of_chinese_yuans = float(input())
commission = float(input())

money_from_bitcoin = number_of_bitcoins * 1168
money_from_chinese_yuan = (number_of_chinese_yuans * 0.15) * 1.76
money_in_euro = (money_from_bitcoin + money_from_chinese_yuan) / 1.95
commission_sum = money_in_euro * (commission / 100)

result = money_in_euro - commission_sum

print(f"{result:.2f}")