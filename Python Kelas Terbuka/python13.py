#operasi dan manipulasi string 

#1. menyambung string
nick_name = "humming bird"
first_name = "jayjo"
last_name = "windbreaker"
full_name = nick_name + " "+ first_name + " " + last_name
print(full_name)
print('---------------------')

#2.menghitung panjang string
panjang = len(full_name)
print("hasinya adalah : " + str(panjang))

#3.operator untuk string

#mengecek apakah ada komponen char atau string di string
x = "bird"
y = x in full_name #penggunaan in
print(y)

x = "jayjo"
y = x not in full_name #penggunaan not in
print(y)
print('---------------------')

#pengulangan string 
print(15*"wk")
print('wk'*15)
print('---------------------')

#indexing
print("mencari index yg ada di full_name[0]:", full_name[0])
print("mencari index yg ada di full_name[1]:", full_name[1])
print("mencari index yg ada di full_name[-1]:", full_name[-1])
print("mencari index yg ada di full_name[-2]:", full_name[-2])
print("mencari index yg ada di full_name[0:11]:", full_name[0:12])
print("mencari index yg ada di full_name[13:29]:", full_name[13:29])
print("mencari index yg ada di full_name[0,2,4,6,8]:", full_name[0:10:2])

print('---------------------')

#item paling kecil
print("item paling kecil:" + min(full_name))#paling kecil dimulai dari '...' (spasi)
#item paling besar
print("item paling besar:" + max(full_name))#(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)

#mencari tahu niali yang paling kecil dan besar
ascii_code = ord("y")
print("mencari nilai y:" + str(ascii_code))
data = 121#nomor yg tadi sudah dicari di (ord)
print("mencari nilai spasi:" + chr(data))
print('---------------------')

#operator dalam bentuk method
name = "Mizzura higasino chan"
name = name.count("a")#mencari ada berapakah jumlah huruf (a) pada (name)
print(name)