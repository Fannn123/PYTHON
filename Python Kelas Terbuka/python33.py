# #looping dari list

# #for loop
# print(20*" "+'FOR LOOP'+"\n")
# kumpulan_data = [1,3,4,10,5,3,]

# for angka in kumpulan_data:
#     print(f"angka = {kumpulan_data}")
# print("\n")  
    
# data_nama = ["saski","shakir","sule"]

# for nama in data_nama:
#     print(f"nama = {data_nama}")
# for nama in data_nama:
#     print(f"nama = {data_nama}")
# print("\n")  


# kumpulan_data = [1,3,4,10,5,3,]
# panjang = len(kumpulan_data)

# for i in range(panjang):
#     print(f"angka = {kumpulan_data[i]}")
# print("\n")  

# #while loop
# print(20*" "+'while loop'+"\n")
# kumpulan_data = [1,3,4,10,5,3,]
# panjang = len(kumpulan_data)
# i = 0

# while i < panjang:
#     print(f"angka = {kumpulan_data[i]}")
#     i += 1

#list comprehesion
print("\n"+20*" "+'comprehesion'+"\n")
data = ["yusuf",1,2,3,"arhan"]

[print(f"data comprehesion= {i}") for i in data]
print("\n")
##
kumpulan_data = [1,3,4,10,5,3,]
data = [i**2 for i in kumpulan_data]

print(f"data pangkat = {data}")


#enumerate
print("\n"+20*" "+'enumerate'+"\n")
data_list= ["yusuf",1,2,3,"arhan"]

for index,data in enumerate(data_list):
    print(f"index = {index} data = {data}")

