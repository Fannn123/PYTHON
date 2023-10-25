'''FUNGSI DENGAN ARGUMENT'''
import os

os.system('cls')
def hello_world(nama):
    print(f"Siapa Nama Kamu: {nama}")

hello_world("nama saya zaki demong")

print('\n')

def matematika(angka1,angka2):
    penjumlahan = angka1 + angka2
    print(f"{angka1} + {angka2} = {penjumlahan}")
    
matematika(2,5)

print('\n')

def kumpulan_data(names):
    data = names.copy() #kalau tidak menggunakan copy data yg diluar fungsi akan ikut keganti
    for x in names:
        print(f"Nama Saya\t:{x}")
    
anggota = ["udin", "asep", "supri"]
kumpulan_data(anggota) #SETIAP APAPUN YG DI ISI DIDALAM ARGUMEN MAKA NILAINYA AKAN SAMA SEPERTI NILAI ARGUMENT(names)