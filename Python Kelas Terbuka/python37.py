#oprasional dictionary

data_dict = {
    'manggo' : 'mangga',
    'orange' : 'jeruk',
    'apple' : 'apel',
    'banana' : 'pisang'
}
#panjang dictionary
LENDICT = len(data_dict)
print(f"data LENDICT: {LENDICT}\n")


#mengecek key exsit atau tidak
KEY = 'apple'
KEY in data_dict
print(f"data KEY: {KEY}\n")

#mengakses value (read) dengan get
print(data_dict['manggo'])
print(data_dict.get('orange'))
print(data_dict.get('melon'))#ketika ada key yg tidak ada secara otomatis akan menghasilkan kata none
print("\n")

#mengupdate data
data_dict['manggo'] = "pineapple"
print(f"{data_dict}\n") #mengganti secara biasa tetpi jika ada yg salah akan langsung eror

data_dict.update({'apple' : 'apel'}) #jika key nya sama makan akan menghasilkan hasil yg sama
print(f"{data_dict}\n")
data_dict.update({'jackfruit' : 'nangka'}) #sedangkan jika key nya tidak ada dalam program secara otomatis akan dibuat
print(f"{data_dict}\n")

#menghapus data
del data_dict["banana"]
print(f"{data_dict}")


