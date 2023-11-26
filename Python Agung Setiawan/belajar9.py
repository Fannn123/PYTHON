#PERCABANGAN if
is_morning = False
is_night = True

#MESSAGE:
#(elif) INI AKAN DIEKSEKUSI JIKA NILAI DARI (if) ADALAH (False) DAN NILAI is_night ADALAH (True)
#APABILA (is_morning) dan (is_night) bernilai (True) MAKA YANG AKAN DIEKSEKUSI ADALAH (is_morning) 

if is_morning: #AKAN DI EKSEKUSI APABILA BENAR(True) DAN TIDAK AKAN DI EKSEKUSI APABILA SALAH(False) 
    print("selamat pagi")
elif is_night:#elif(is_night) BERFUNGSI UNTUK KONDISI TAMBAHAN
    print("selamat malam")
else: #FUNGSI else DISINI ADALAH KARENA SEBAGAI ALTERNATIF KETIKA FUNGSI if(is_morning) TIDAK BEKERJA                         
    print("selamat sore")
print("selamat beraktifitas")#AKAN SELALU DIEKSEKUSI "selamat beraktifitas" KARENA DILUAR PENGKONDISIAN if dan else
 



   
 