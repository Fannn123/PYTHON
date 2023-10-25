'''DEFAULT ARGUMENT'''


#contoh 1
def fungsi(nama = "hallo tamfan"):
    print(f"Nama Saya adalah: {nama}")
    
fungsi("usup") #normal
fungsi() #menggunakan DEFAULT ARGUMENT
print('\n')


#contoh 2
def human(nama,pesan = 'saya suka rokok'):
    print(f"nama saya: {nama} {pesan}")
    
human('usup','Saya suka makan') # normal
human('sahrul') #menggunakan default argument
print('\n')


#contoh 3
def bilangan_pangkat(angka,pangkat = 2):
    pngkt = angka**pangkat
    return pngkt

print(bilangan_pangkat(5,2)) #normal

x = bilangan_pangkat(angka = 5,pangkat = 3) #menggunakan default argument
print(f"{x}")
print('\n')


#contoh 4
def input_user(input1 =2 ,input2 =1 ,input3 =4, input4 =3):
    data = input1 + input2 + input3 + input4
    return data

print(input_user()) #normal
print(input_user(input3 = 10)) #menggunakan default argument

