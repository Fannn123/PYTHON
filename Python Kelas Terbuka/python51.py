##GLOBAL DAN LOCAL SCOPE

nama_orang = "yudi" # <-- INI ADALAH GLOBAL BERADA DILUAR

#akses variable global dalam fungsi
def fungsi():
    print(f"saya adalah : {nama_orang}")
fungsi()
print('-'*20)

#akses variabel global dalam loop
for x in range(0,5):
    print(f"nomor {x} --> adalah {nama_orang}")
print('-'*20)

#dengan percabangan
if True:
    print(f"nama a'ne : {nama_orang}")  
print('-'*20)
print('\n')



##VARIABLE LOCAL SCOPE
def fungsi2():
    nama = "sarminah" # <-- INI ADALAH VARIABLE LOCAL SCOPE BERADA DIDALAM
    
fungsi()
# print(nama) <-- JIKA SEPERTI INI SALAH 

#contoh 1 penggunaan akses variable
def say_hallo():
    print(f"nama saya {nama}")
    
nama = "zaki"
say_hallo()
print('\n')

#contoh 2 merubah variable global
angka = 0
name = "supri"

def variable(nilai,nama):
    global angka 
    angka = nilai
    global name 
    name = nama
    
print(f"sebelum diubah : {angka,name}") 
 
variable(100,'asep') 
print(f"setelah diubah : {angka,name}") 
print('\n')

#contoh 3 
'''VARIABLE GLOBAL DAPAT DIUBAH TAMPA HARUS MEMANGGIL (global) KETIKA MENGGUNAKAN PERULANGAN DAN KONDISI '''
angka = 0

for y in range(0,5):
    angka += y
    angka_dummy = 0
    
if True:
    angka = 10
    angka_dummy = 50
    print(angka)
    print(angka_dummy)