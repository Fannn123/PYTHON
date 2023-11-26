#general exception
try:
  user = input("masukan level anda : ")#jika ada perintah yg diberikan selain (angka),seharusnya eror karena menggunakan tyr dan except makan akan mengeksekusi kata  "silahkan coba lagi"
  user = int(user)
  
  print(user)
  
except:#untuk memberikan perintah jika ada kesalahan dalam program yg tidak sesuai maka akan mengeksekusi kata "silahkan coba lagi"
    print("silahkan coba lagi") 
    