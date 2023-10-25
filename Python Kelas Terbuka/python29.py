data_angka = [1,2,4,7,3,9,4,3,9,0,3,5,9,]
print(f"data angka = {data_angka}")

#count data
data_angka_3 = data_angka.count(3)
data_angka_4 = data_angka.count(4)
data_angka_9 = data_angka.count(9)

print(f"ada berapa data 3 = {data_angka_3}")
print(f"ada berapa data 4 = {data_angka_4}")
print(f"ada berapa data 9 = {data_angka_9}")
print("\n")


#ambil posisi data (index)
name = ["arhan", "muslih", "supri"]

index_0 = name.index("arhan")
index_1 = name.index("muslih")
index_2 = name.index("supri")

print(f"index 'arhan' adalah = {index_0}")
print(f"index 'muslih' adalah = {index_1}")
print(f"index 'supri' adalah = {index_2}")
print("\n")


#mengurutkan list menggunakan sort
## mengurutkan angka
data_angka.sort() #mengurutkan data dari yg terkecil hingga terbesar
print(f"mengurutkan angka dimulai dari = {data_angka}")
## mengurutkan huruf 
name.sort() #mengurutkan huruf dari yg terkecil hingga terbesar
print(f"mengurutkan huruf dimulai dari = {name}")
print("\n")


#balik list nya
data_angka.reverse()
name.reverse()#mengurutkan data dari yg terbesar hingga terkecil
print(f"membalikan dimulai dari = \n{data_angka} \n {name}")

