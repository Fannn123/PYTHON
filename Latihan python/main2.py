#SHOPPING CART PROGRAM
import os

food = []
total = 0 
price = []

os.system('cls')
while True:
    foods = input("=> buy a food (q to quit): ")
    if foods.lower() == "q":
        break
    else:
       prices = float(input(f"<=> the price of a {foods}: $"))
       food.append(foods)
       price.append(prices)
  
print("-"*30) 
print(f"{'YOUR CART':^30}")   
print("-"*30) 

for index,foods in enumerate(food):
    print(f'{index+1}.{foods}')
print()   
  
for prices in price:
    total += prices
print(f'your total is: ${total}')
