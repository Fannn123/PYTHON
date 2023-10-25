'''**KWARGS'''

def contoh_1(**kwargs):
    print(kwargs)
    
contoh_1(buah = "nanas",benda = "meja",makanan = "nasi") #akan menghasilkan bentuk dictonary
print('\n')


def contoh_2(**data):
    buah = data["buah"]
    benda = data["benda"]
    makanan = data["makanan"]
    print(f"'Buah':{buah} 'Benda':{benda} 'Makanan':{makanan}")
    
contoh_2(buah = "anggur",benda = "pensil",makanan = "salmon")
print('\n')


def math(*args,**kwargs):
    output = 0
    if kwargs["opsional"] == "tambah":       
      for angka in args:
        output += angka
    
    elif kwargs["opsional"] == "kali":
      output = 1
      for angka in args:
          output *= angka
          
    else:
        print("PROGRAM SELESAI") 
        
    return output

hasil = math(1,2,3,opsional = "tambah")
print(f"hasil  dari penjumlahan = {hasil}")

hasil = math(1,2,3,opsional = "kali")
print(f"hasil  dari perkalian = {hasil}")


        
    
        