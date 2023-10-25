# MEMBUAT PACKAGE
from package import matematika
# from package.matematika import penjumlahan as tambah
# from package.matematika import perkalian as kali
# from package.matematika import perpangkatan as pangkat

opsi1 = matematika.penjumlahan(10,9)
print(f"hasil penjumlahan : {opsi1}") 

opsi2 = matematika.perkalian(9,9)
print(f"hasil perkalian : {opsi2}") 

opsi3 = matematika.perpangkatan(2)
print(f"hasil penjumlahan : {opsi3(3)}") 