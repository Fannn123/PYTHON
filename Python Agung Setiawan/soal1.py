print("soal nomor-1")

# Buatlah sebuah fungsi bernama 'greeting' yang menerima satu parameter 'nama' dan mencetak pesan sambutan.
# Contoh, jika parameter 'nama' adalah "Alice", maka fungsi akan mencetak "Halo, Alice!"

# Tulis fungsi 'greeting' di sini

# Panggil fungsi dengan nama "Alice"
def greeting(nama):
    print(F"hallo {nama}")
greeting("alice")

print("\nsoal nomor-2")

# Buatlah sebuah fungsi bernama 'luas_lingkaran' yang menerima jari-jari lingkaran dan mengembalikan luasnya.
# Gunakan nilai π (pi) sebagai 3.14.
# Contoh, jika jari-jari adalah 5, maka fungsi akan mengembalikan 78.5

# Tulis fungsi 'luas_lingkaran' di sini

# Panggil fungsi dengan jari-jari lingkaran 
def luas_lingkaran(jari_jari):
   return 3.14 * jari_jari * jari_jari

luas_jari_jari = 5
luas = luas_lingkaran(luas_jari_jari)
print(f"luas lingkaran dengan jari {luas_jari_jari} adalah {luas}")

print("\nsoal nomor-3")
# Buatlah sebuah fungsi bernama 'hitung_kata' yang menerima sebuah string kalimat dan menghitung jumlah kata dalam kalimat tersebut.
# Anggap setiap kata dipisahkan oleh spasi.
# Contoh, jika kalimat adalah "Ini adalah sebuah kalimat", maka fungsi akan mengembalikan 5.

# Tulis fungsi 'hitung_kata' di sini

# Panggil fungsi dengan kalimat "Ini adalah sebuah kalimat"
def hitung_kata(hitung):
    name = len("irfan")
    print(f"{hitung} {name}")
    return

hitung_kata("ini adalah sebuah kalimat")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print("\n------------")
    
    
def hitung_kata(kalimat):
      kata_list = kalimat.split()  # Memisahkan kata-kata dalam kalimat berdasarkan spasi
      jumlah_kata = len(kata_list)  # Menghitung jumlah kata dalam kalimat
      return jumlah_kata

# Panggil fungsi dengan kalimat "Ini adalah sebuah kalimat"
kalimat_input = "Ini adalah sebuah kalimat"
jumlah_kata = hitung_kata(kalimat_input)
print("Jumlah kata dalam kalimat adalah", jumlah_kata)
