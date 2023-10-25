# break

# CARA 1
angka = 0 

while angka < 5:
    angka += 1
    print(angka)
    
    if angka == 3:
        print("wwwoooowww")
        break # KETIKA ANGKA 3 == 3 SECARA OTOMATIS PROGRAM AKAN LANGSUNG BERHENTI WALAUPUN ADA BEBERAPA PROGRAM YG BELUM DISEBUTKAN
    print("NICE!!!!")

print("END PROGRAM")

# # CARA 2 
# user = int(input("MASUKAN ANGKA:"))

# angka = 0

# while True:
#     angka +=1 
#     print(f"ini angka: {angka}")
    
#     if angka == user:
#         print(f"LOL!!!! {angka}")
#         break
#     print("Nice!!!")
    
# print("END PROGRAM")