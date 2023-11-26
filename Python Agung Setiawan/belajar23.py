#KEYWORD ARGUMENT 
def Harga_barang(uang, kembalian, discount):
    print(f"jadi totanya adalah :  {uang} {kembalian} {discount}")
    
Harga_barang("50", "100.000", "50.000") #TIDAK MENGGUNAKAN KEYWORD ARGUMENT (TIDAK SESUAI DENGAN PARAMETER/BERANTAKAN)

Harga_barang(uang=100.000, kembalian=50.000, discount=50) #MENGGUNAKAN KEYWORD ARGUMENT (MENJADI TERSUSUN RAPIH DAN SESUAI DENGAN ARGUMEMNT)