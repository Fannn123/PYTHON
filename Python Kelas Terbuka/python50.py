'''LAMBDA FUNCTION'''

#NORMAL 
def fungsi_kuadrat(angka):
    return angka**2

print(f"hasil normal = {fungsi_kuadrat(5)}")
print('\n')

#KITA COBA DENGAN LAMBDA
#output = lambda argument : expression

#contoh 1
pangkat = lambda nomor : nomor**2
print(f"hasil lambda = {pangkat(10)}")
#contoh 2
pangkat = lambda number,rank : number**rank
print(f"hasil lambda = {pangkat(9,2)}")
print('\n')

#KEGUNAAN BUAT APA?

#SORTING UNTUK LIST BIASA
data_list = ['cecep','yumi','gaang']
data_list.sort()
print(f"data sort: {data_list}")
print('-'*30)

#SORTING MENGGUNAKAN PANJANG(len)
def fungsi(nama):
    return len(nama)

data_list.sort(key=fungsi)
print(f"data sort by panjang(len) = {data_list}")
print('-'*30)

#SORT MENGGUNAKAN LAMBDA
data_list = ['cecep','yumi','gaang']
data_list.sort(key=lambda nama : len(nama))
print(f"data lambda = {data_list}")
print('-'*30)


#FILTER
data_angka = [1,2,3,4,5,6,7,8,9,10]

def kurang_dari_lima(angka):
    return angka < 6

# contoh1
data_baru1 = list(filter(kurang_dari_lima,data_angka))
print(F"INI ADALAH DATA BARU1 = {data_baru1}")
# contoh2
data_baru2 = list(filter(lambda x : x<6, data_baru1))
print(F"INI ADALAH DATA BARU1 = {data_baru2}")
print('\n')

#kasus genap
data_genap = list(filter(lambda y : (y%2==0),data_angka))
print(f"data genap = {data_genap}")
#kasus ganil
data_ganjil = list(filter(lambda y : (y%2!=0),data_angka))
print(f"data ganjil = {data_ganjil}")
#kelipatan 3
data_kelipatan3 = list(filter(lambda y : (y%3==0),data_angka))
print(f"data kelipatan 3 = {data_kelipatan3}")
print('\n')

#ANONYMOUSE FUNCTION
#CURRYING <-- HASKELL CURRY

def data(angka,n):
    hasil = angka**n
    return hasil
data_hasil = data(10,2)
print(f"fungsi biasa = {data_hasil}")
print('\n')

#DENGAN CURRYING 
def pangkat(n):
    return lambda angka : angka**n

#contoh1
pangkat2 = pangkat(2)
print(f"hasil pangkat2 = {pangkat2(5)}")
print('-'*30)
#contoh2
pangkat3 = pangkat(3)
print(f"hasil pangkat3 = {pangkat3(3)}")
print('-'*30)
#contoh3
print(f"hasil pangkat bebas = {pangkat(4)(5)}")



