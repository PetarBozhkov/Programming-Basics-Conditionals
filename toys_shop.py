excursion_price = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())
toys_price = num_trucks * 2 + num_minions * 8.20 + num_bears * 4.10 + num_dolls * 3 + num_puzzles * 2.60
if toys_price >= 50:
    print(toys_price * 0.25)
rent = toys_price * 0.1
profit = toys_price - rent
money_left = abs(profit - excursion_price)

if money_left >= excursion_price:
    print(f"Yes! {money_left} lv left.")
else:
    print(f"Not enough money! {money_left} lv needed.")