package_weight = float(input())
type_of_service = input()
distance_in_kms = int(input())

price_for_km = 0.03

if 1 <= package_weight < 10:
    price_for_km = 0.05
elif 10 <= package_weight < 40:
    price_for_km = 0.10
elif 40 <= package_weight < 90:
    price_for_km = 0.15
elif 90 <= package_weight:
    price_for_km = 0.20

express_price = 0

if type_of_service == "express":
    if 1 > package_weight:
        express_price = 0.8
    if 1 < package_weight < 10:
        express_price = 0.4
    elif 10 <= package_weight < 40:
        express_price = 0.05
    elif 40 <= package_weight < 90:
        express_price = 0.02
    elif 90 <= package_weight:
        express_price = 0.01
    express_price *= price_for_km

total_price = (price_for_km + package_weight * express_price) * distance_in_kms

print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {total_price:.2f} lv.")