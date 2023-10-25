import random
import os
import string

kamus = {
    "banana" : "pisang",
    "grape" : "anggur",
    "jackfruit" : "nangka",
    "coconut" : "kelapa",
    "guava" : "jambu biji"
}
while True:
  user = input("Ingin Cari Arti Apa?\t")
  
  print(f"\n{'DICTIONARY INGLISH':^50}")
  print(f"{'INGLISH -> INDONESIA':^50}")
  
  print("-"*54)
  print(f"{'|':<3} {'KEY':<5} {'|'} {'INGLISH':^20} {'|'} {'INDONESIA':^17} {'|'}")
  print("-"*54)
  
  # verb = dict.fromkeys(kamus.keys())
  
  data_kosong = {}
  
  KEY = " ".join(random.choice(string.ascii_uppercase) for x in range(2))
  # data_kosong.update({KEY:user})
  
  if user== "banana":
   x = kamus.setdefault("banana")
   print(f"{'|':<3} {KEY:<5} {'|'} {'banana':^20} {'|'} {x:^17} {'|'}")
 
  elif user== "grape":
   x = kamus.setdefault("grape")
   print(f"{'|':<3} {KEY:<5} {'|'} {'grape':^20} {'|'} {x:^17} {'|'}")
   
  elif user== "jackfruit":
   x = kamus.setdefault("jackfruit")
   print(f"{'|':<3} {KEY:<5} {'|'} {'jackfruit':^20} {'|'} {x:^17} {'|'}")
   
  elif user== "coconut":
   x = kamus.setdefault("coconut")
   print(f"{'|':<3} {KEY:<5} {'|'} {'coconut':^20} {'|'} {x:^17} {'|'}")
   
  elif user== "guava":
   x = kamus.setdefault("guava")
   print(f"{'|':<3} {KEY:<5} {'|'} {'guava':^20} {'|'} {x:^17} {'|'}")
   
   
