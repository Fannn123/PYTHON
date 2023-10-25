# continue

angka = 0

while angka < 5:
    angka +=1
    print(angka)
    
    if angka == 3:
        print("owowoowww") # INI AKAN DI EKSEKUSI APABILA ANGKA TIGA SAMA DENGAN TIGA
        continue # TIDAK AKAN MENGEKSEKUSI PERINTAH YG ADA DIBAWAHNYA
    print("LOL") # LOL INI AKAN DILEWAT KETIKA ANGKA 3 == 3 
    
print("END PROGRAM")