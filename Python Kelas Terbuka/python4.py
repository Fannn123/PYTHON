#input user

#data yang dimasukan pasti string
data = input("masukan data : ")

print("data : ", data, "tipenya : ", type(data))

#jika kita ingin mengambil int 
data = int(input("masukan data : "))
data = float(input("masukan data : "))

print ("data : ", data, "tipenya : ", type(data))
print ("data : ", data, "tipenya : ", type(data))

#bagaimana dengan boolean
biner = bool(int(input("masukan data : ")))

print("data : ", biner, "tipenya : ", type(biner))