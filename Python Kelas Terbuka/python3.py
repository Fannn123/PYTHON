#belajar casting
#merubah dari satu tipe ketipe yang lain
#tipe data : str,float,bool,int
print("====INTEGER====")
data_int = 9
print("data : ", data_int)

data_float = float(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0
data_str = str(data_int)

print("data float : ", data_float)
print("data bool : ", data_bool)
print("data str : ", data_str)


print("====FLOAT====")
data_float= 9.9
print("data : ", data_float)

data_int = int(data_float)#akan dibulatkan kebawah
data_bool = bool(data_float) #akan false jika nilai float = 0c
data_str = str(data_float)

print("data int : ", data_int)
print("data bool: ", data_bool)
print("data str : ", data_str)



print("====BOOL====")
data_bool= True
print("data : ", data_bool)

data_int = int(data_bool)#akan dibulatkan kebawah
data_float = float(data_bool) 
data_str = str(data_bool)

print("data int : ", data_int)
print("data float: ", data_float)
print("data str : ", data_str)


print("====STRING====")
data_str= "10"
print("data : ", data_str)

data_int = int(data_str)#akan dibulatkan kebawah
data_float = float(data_str) 
data_bool = bool(data_str)

print("data int : ", data_int)
print("data float: ", data_float)
print("data bool : ", data_bool)
