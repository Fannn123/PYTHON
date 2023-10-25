#operasi komparasi
#setiap hasil komparasi adalah boolean
#<,>,<=,>=,==,!=,is,is not

a = 4
b = 2

print("==========KURANG DARI (<)==========")
hasil = a < 3
print("hasilnya : ", hasil)
hasil = b < 3
print("hasilnya : ", hasil)
hasil = b < 2
print("hasilnya : ", hasil)

print("==========LEBIH DARI (>)==========")
hasil = a> 3
print("hasilnya : ", hasil)
hasil = b> 3
print("hasilnya : ", hasil)
hasil = b> 2
print("hasilnya : ", hasil)

print("==========KURANG DARI SAMA DENGAN (<=)==========")
hasil = a <= 3
print("hasilnya : ", hasil)
hasil = b <= 3
print("hasilnya : ", hasil)
hasil = b <= 2
print("hasilnya : ", hasil)

print("==========LEBIH DARI SAMA DENGAN (>=)==========")
hasil = a >= 3
print("hasilnya : ", hasil)
hasil = b >= 3
print("hasilnya : ", hasil)
hasil = b >= 2
print("hasilnya : ", hasil)

print("========== SAMA DENGAN (==)==========")
hasil = a == 4
print("hasilnya : ", hasil)
hasil = b == 4
print("hasilnya : ", hasil)

print("==========TIDAK SAMA DENGAN (!=)==========")
hasil = a != 4
print("hasilnya : ", hasil)
hasil = b != 4
print("hasilnya : ", hasil)

print("==========OBJECT IDENTITY (is)==========")
#'is' sebagai komparasi objeci identity
x = 5 #ini adalah assingment pembuat object
y = 5
print("nilai x :", x, "id :", hex(id(x)))
print("nilai y :", y, "id :", hex(id(y)))

hasil = x is y
print("hasilnya : ", hasil)

print("==========OBJECT IDENTITY (is NOT)==========")
#'is' sebagai komparasi objeci identity
x = 5
y = 5
print("nilai x :", x, "id :", hex(id(x)))
print("nilai y :", y, "id :", hex(id(y)))

hasil = x is not y
print("hasilnya : ", hasil)