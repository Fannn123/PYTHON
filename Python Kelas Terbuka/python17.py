import datetime 

print("silahkan masukan: \n1.tanggal \n2.bulan \n3.tahun")
tanggal = int(input("tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("tahun \t\t:"))

tahun_lahir = datetime.date(tahun, bulan, tanggal)
print(f"TAHUN LAHIR ANDA ADALAH: {tahun_lahir}")
print(f"HARINYA ADALAH: {tahun_lahir:%A}")
print("\n"+15*"-"+"pembatas"+"-"*15+"\n")

hari_ini = datetime.date.today()
print(F"HARI INI TANGGAL: {hari_ini}")

umur_hari = hari_ini - tahun_lahir
umur_tahun = umur_hari.days // 366
print(f"UMUR ANDA: {umur_tahun} TAHUN")