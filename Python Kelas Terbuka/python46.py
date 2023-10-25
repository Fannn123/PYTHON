# latihan fungsi
# Menghitung luas dan Keliling Persegi panjang


import os

# #Membuat Header Program
# os.system('cls')
# print(F"{'PROGRAM LATIHAN FUNGSI':^40}")
# print(F"{'MENGHITUNG LUAS PERSEGI PANJANG':^40}")
# print('-'*39)

# #STATEMENT1
# #Menerima Input Dari User
# lebar = int(input('Panjangnya Berapa\t\t:'))
# panjang = int(input('Lebarnya Berapa\t\t\t:'))

# #STATEMENT2
# #Menghitung Luas dan Keliling
# luas = panjang * lebar
# keliling = 2*(panjang+lebar)

# #STATEMENT3
# #Mengeluarkan Hasil Perhitungan
# print(f"hasil persegi panjang\t\t:{luas}")
# print(f"hasil keliling persegi panjang \t:{keliling}")


# #Membuat Header Program
def header():
    '''MEMBUAT HEADER'''
    os.system('cls')
    print(F"{'PROGRAM LATIHAN FUNGSI':^40}")
    print(F"{'MENGHITUNG LUAS PERSEGI PANJANG':^40}")
    print('-'*39)
    
# #Menerima Input Dari User
def input_user():
    '''MENERIMA INPUT USER'''
    lebar = int(input('Panjangnya Berapa\t\t:'))
    panjang = int(input('Lebarnya Berapa\t\t\t:'))
    return panjang,lebar

# #Menghitung Luas 
def hasil_luas(panjang,lebar):
    '''MENGHITUNG LUAS'''
    return panjang * lebar

# #Menghitung Keliling
def hasil_keliling(panjang,lebar):
    '''MENGHITUNG KELILING'''
    return 2*(panjang + lebar)

# #Mengeluarkan Hasil Perhitungan
def display(message,value):
    '''MENAMPILKAN HASIL'''
    print(f"hasilnya perhitungan {message}\t= {value}")
 
 
while True:
    
    #membuat header
    header()
    
    
    #menerima input user
    lebar,panjang = input_user()
    
    
    #1
    #mencari nilai luas
    luas = hasil_luas(panjang,lebar)
    #2
    #mencari nilai keliling
    keliling = hasil_keliling(panjang,lebar)
    
    
    #menampilkan hasil
    display("luas",luas)
    display("keliling",keliling)
    
    user = input("Apakah Ingin Lanjut(y/n)? ")
    if user == "n":
        break