import os

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
def hasil_keliling(panjang,lebar):
    '''MENGHITUNG KELILING'''
    return 2*(panjang + lebar)

# #Menghitung Keliling
def hasil_luas(panjang,lebar):
    '''MENGHITUNG LUAS'''
    return panjang * lebar

# #Mengeluarkan Hasil Perhitungan
def display(message,value):
    '''MENAMPILKAN HASIL'''
    print(f"hasil perhitungan {message}\t= {value}")
 
 
while True:
    
    header()
    
    pilihan = input("ingin menghitung apa?(luas/keliling)\t:")
    if pilihan == "luas":
        
       panjang,lebar = input_user()
       luas = hasil_luas(panjang,lebar)
       display("luas",luas)
    
    elif pilihan == "keliling":
       panjang,lebar = input_user()
       keliling = hasil_keliling(panjang,lebar);
       display("keliling",keliling)
       
        
    x = input("\napakah ingin lanjut(y/n)?\t")
    
    if x == "n":
        break
    
     