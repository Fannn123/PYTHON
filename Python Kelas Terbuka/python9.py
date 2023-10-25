#latihan logika dan komparasi
#membuat gabungan area rentang dari angka

#+++++3-----10+++++

user = float(input("masukan angka : "))

#memerikasa angka kurang dari 3
#+++++3-----
kurang_dari = user < 3
print("kurang dari 3 :",kurang_dari)
print("\n ========== \n")

#memerikasa angka lebih dari 10
#-----10+++++
lebih_besar_dari = user > 10
print("kurang dari 10 :",lebih_besar_dari)

#+++++3-----10+++++
correct = kurang_dari or lebih_besar_dari
print("hasilnya :",correct)

print("================================================")

#-----3+++++10-----
#kasus irisan

user = float(input("masukan angka : "))

#lebih besar dari 3
#-----3+++++
lebih_besar_dari = user > 3
print("kurang dari 3 : ",lebih_besar_dari)
print("\n ========== \n")

#kurang dari 10
#+++++10-----
kurang_dari = user < 10
print("kurang dari 10 : ",kurang_dari)

correct = kurang_dari and lebih_besar_dari
print("hasilnya : ",correct)