#exception
try:#JIKA TERJADI EROR KETIKA AKAN MENGEKSEKUSI MAKAN MEMBERIKAN PERINTAH "TIDAK DIKENALI"
  user = input("masukan level anda : ")
  user = int(user)
    
  print(user)
except ValueError:
    print("tidak di kenal") 
    