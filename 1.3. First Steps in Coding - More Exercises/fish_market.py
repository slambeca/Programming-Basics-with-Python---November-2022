price_skumria_kg = float(input())
price_caca_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
sea_shells_kg = int(input())

price_palamud = price_skumria_kg + (price_skumria_kg * 0.6)
paid_for_palamud = price_palamud * palamud_kg
price_safrid = price_caca_kg + (price_caca_kg * 0.8)
paid_for_safrid = price_safrid * safrid_kg
paid_for_sea_shells = sea_shells_kg * 7.5

total_sum = paid_for_sea_shells + paid_for_palamud + paid_for_safrid

print(f"{total_sum:.2f}")