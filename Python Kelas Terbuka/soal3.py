print("""
         =================================
                  WARUNG OMENG
              MAKAN MINUMAN DAN ROKOK
         =================================

                   MENU MAKANAN
---------------------------------------------------
| KODE |      NAMA MAKANAN      |      HARGA      |  
---------------------------------------------------
| NS |  NASI TELUR    + SAYUR  |  RP. 15.000      |  
| PN |  PECEL AYAM    + NASI   |  RP. 20.000      |  
| KA |  KIKIL + NASI  + AYAM   |  RP. 25.000      |  
| KL |  SAYUR + NASI  + IKAN   |  RP. 20.000      |  
| SL |  AYAM  + SAYUR + NASI   |  RP. 25.000      |  


                   MENU MINUMAN
---------------------------------------------------
| KODE |      NAMA MINUMAN      |      HARGA      |  
---------------------------------------------------
|  OX  |  ES JERUK              |  RP. 5.000      |  
|  VN  |  ES TEH                |  RP. 5.000      |  
|  KS  |  ES KUWUD              |  RP. 10.000     |  
|  IB  |  ES KELAPA             |  RP. 5.000      |  
|  QL  |  JUS                   |  RP. 10.000     |  


         =================================
                SELAMAT MENIKMATI
         =================================
 """)


print("SILAHKAN INGIN MEMESAN APA?\n\nJIKA MAKAN KETIK 1\nJIKA MINUMAN KETIK 2")
opsi = int(input("\n1/2\t\t:"))
if opsi == 1 or 2:
    kode = input("MASUKAN KODE\t:")
    x = int(input("JUMLAH PESANAN\t:"))

# statment 1
    if kode == "NS":
      print(f"\nKODE\t:{kode} \nPESANAN\t:'NASI TELUR + SAYUR' \njumlah pesanan\t:{x} \nHARGA\t:15.000 \nTOTAL\t:RP.{x*15.000}00\n")
    elif kode == "PN":
      print(f"\nKODE\t:{kode} \nPESANAN\t:'PECEL AYAM + NASI' \njumlah pesanan\t:{x} \nHARGA\t:20.000 \nTOTAL\t:RP.{x*20.000}00\n")
    elif kode == "KA":
      print(f"\nKODE\t:{kode} \nPESANAN\t:'KIKIL + NASI + AYAM' \njumlah pesanan\t:{x} \nHARGA\t:25.000 \nTOTAL\t:RP.{x*25.000}00\n")
    elif kode == "KL":
      print(f"\nKODE\t:{kode} \nPESANAN\t:'SAYUR + NASI + IKAN' \njumlah pesanan\t:{x} \nHARGA\t:20.000 \nTOTAL\t:RP.{x*20.000}00\n")
    elif kode == "SL":
      print(f"\nKODE\t:{kode} \nPESANAN\t:'AYAM SAYUR NASI' \njumlah pesanan\t:{x} \nHARGA\t:25.000 \nTOTAL\t:RP.{x*25.000}00\n")
      
# statment 2

    elif kode == "OX":
        print(f"\nKODE\t:{kode} \nPESANAN\t:'ES JERUK' \njumlah pesanan\t:{x} \nHARGA\t:5.000 \nTOTAL\t:RP.{x*5.000}00\n")
    elif kode == "VN":
        print(f"\nKODE\t:{kode} \nPESANAN\t:'ES TEH' \njumlah pesanan\t:{x} \nHARGA\t:5.000 \nTOTAL\t:RP.{x*5.000}00\n")
    elif kode == "KS":
         print(f"\nKODE\t:{kode} \nPESANAN\t:'ES KUWUD' \njumlah pesanan\t:{x} \nHARGA\t:10.000 \nTOTAL\t:RP.{x*10.000}00\n")
    elif kode == "IB":
        print(f"\nKODE\t:{kode} \nPESANAN\t:'ES KELAPA' \njumlah pesanan\t:{x} \nHARGA\t5.000 \nTOTAL\t:RP.{x*5000}00\n")
    elif kode == "QL":
        print(f"\nKODE\t:{kode} \nPESANAN\t:'JUS' \njumlah pesanan\t:{x} \nHARGA\t:10.000 \nTOTAL\t:RP.{x*10.000}00\n")
      