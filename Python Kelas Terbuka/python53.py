#modul MATEMATIKA dengan import

from MATEMATIKA import OPS_tambah,OPS_kali,OPS_pangkat
from MATEMATIKA import * # <-- gunakan ini untuk mengambil semua modul MATEMATIKA


penjumlahan = OPS_tambah(1,2,3,4,5)
print(f'hasil penjumlahan = {penjumlahan}')

perkalian = OPS_kali(1,2,3,4,5)
print(f'hasil perkalian = {perkalian}')

pangkat_2 = OPS_pangkat(2)
print(f'hasil pangkat = {pangkat_2(5)}')

# #alias
# '''
# 1.harus mengimportnya satu-persatu
# 2.gunanya untuk mengganti nama dan
#   nanti harus menggunakan nama yg telah diganti untuk memanggil modul
# '''

# from MATEMATIKA import OPS_tambah as penjumlahan
# from MATEMATIKA import OPS_kali as perkalian
# from MATEMATIKA import OPS_pangkat as perpangkatan

# penjumlahan = perpangkatan(1,2,3,4,5) #yg tadinya bernama OPS_pangkat sekarang menjadi perpangkatan
# print(f'hasil penjumlahan = {penjumlahan}')
 