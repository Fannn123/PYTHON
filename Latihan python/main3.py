import os

menu = {"pizza":8.00,
        "pasta":5.40,
        "hotdog":5.6,
        "colla":2.1,
        "soda":2.20,
        "beer":2.54}

cart = []
total = 0

os.system("cls")

print("------- MENU -------")
for key,value in menu.items():
    print(f"~ {key:10}: ${value:.2f}")
print("--------------------")
    
while True:
    user = input("ingin pesan apa (q to quit): ").lower()
    if user == "q":
        break
    
    elif menu.get(user) is not None: # -> jika result yg dihasilkan tidak ada pada menu maka akan menghasilakan None
         cart.append(user)

print()
print("---- YOUR ORDER ----")
for index,food in enumerate(cart): # melooping sesuai banyanyak jumlah(cart)
   total += menu.get(food) # mengambil (key pada menu) untuk dijumlahkan
   print(f"{index+1}.{food}")

print()
print(f"totals is: ${total:.2f}")
