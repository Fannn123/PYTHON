'''FUNGSI DENGAN PENGEMBALIAN'''

def fungsi(angka1):
    pangkat = angka1**2
    return pangkat
    
x = fungsi(2)
print(f"hasil pangkat*2 = {x}")
print(f"hail pangkat*5 {fungsi(5)}")

z = 10 + fungsi(5)
print(f"hasil 10 +(5*2) adalah = {z}")
print('\n')


def penjumlahan(angka1,angka2):
    return angka1 + angka2

y = penjumlahan(10,30)
print(f"hasil penjumlahan 10 + 30 = {y}")
print('\n')


#fungsi dengan return banyak
def operasi_matematika(operasi1,operasi2):
    tambah = operasi1 + operasi2
    kurang = operasi1 - operasi2
    kali = operasi1 * operasi2
    bagi = operasi1 / operasi2
    
    return tambah,kurang,kali,bagi

a,b,c,d = operasi_matematika(30,5)

print(f"hasil penjumlahan = {a}")
print(f"hasil pengurangan = {b}")
print(f"hasil perkalian = {c}")
print(f"hasil pembagian = {d}")