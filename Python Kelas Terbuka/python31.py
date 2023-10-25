#netled list

data0 = [1,2]
data1 = [3,4]
data2 = [5,6,7,8,9]

data_3D = [data0,data1,data2]
print(data_3D)
print("\n")

#contoh penggunaan 
absen1 = ["yusuf", 22, "pria"]
absen2= ["akane", 19, "perempuan"]
absen3 = ["sizuka", 20, "perempuan"]

gabungan = [absen1,absen2,absen3]
print(f"{gabungan}\n")

for x in gabungan:
    print(f"Nama\t\t:{x[0]}")
    print(f"Umur\t\t:{x[1]}")
    print(f"Gender\t\t:{x[2]}\n")
    
    
copy = gabungan.copy()
print(f"hasil copy\t:{copy}")

absen1[0] = "arhan"
print(f"hasil sesudah dicopy\t:{copy}")
print(f"hasil sesudah dicopy\t:{gabungan}")

print(f"hasil sesudah dicopy\t:{hex(id(copy))}")
print(f"hasil sesudah dicopy\t:{hex(id(gabungan))}")

