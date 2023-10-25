sisi = 10
count = 1

# 1.MENGGUNAKAN FOR
#dummyfariabel
# for i in range(sisi):
#     print("*"*count)
#     count += 1

# print("END PROGRAM\N")

# 2.MENGGUNAKAN WHILE
# while True:
#     print("*"*count)
#     count += 1
    
#     if count == sisi:
#         break

# print("END PROGRAM\N")    

# # 3.SEGITIGA GANJIL
# while True:
#     if (count%2):
#         #print jika ganjil
#       print("*"*count)
#       count += 1
    
#     else: 
#         # akan kembali keatas jika ganjil
#         count +=1
#         continue
    
#     #akan break jika count lebih dari sisi
#     if count > sisi:
#         break
    
# print("END PROGRAM\N")  

# 4.SIGITIGA SAMA KAKI
spasi = int(sisi/2)

while True:
    if (count%2==1):
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
        
    else:
        count += 1
        continue
    
    if count > sisi:
        break
     

spasi = 1
sisi = 1
count = 10

while True:
    if(count%2==0):
        count -= 1
        print(" "*spasi,"*"*count)
        spasi += 1
        
    else :
        count -= 1
        continue
    
    if count <= sisi :
        break
        

print("END PROGRAM")  
     