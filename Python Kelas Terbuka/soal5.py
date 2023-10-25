import datetime
import os
import random
import string

data = {
    'Nama':"aaaaaa",
    'Kelas':'13 TOI 2',
    'Umur':'19 tahun',
    'Tanggal lahir': datetime.datetime(1111,1,11)
}

data_baru = {}

while True:
  os.system("cls")
  
  print(f"{'WELCOME TO CLASS 13 OTOMASI INDUSTRI':^20}")
  print(f"{'ABSENSI CLASS 13 TOI 2':^20}")
  print("-"*30)
  print("\n")

  absen = dict.fromkeys(data.keys())

  absen['Nama'] = input("Nama(Siswa/Siswi)\t:")
  absen['Kelas'] = input("Kelas\t\t\t:")
  absen['Umur'] = input("Umur\t\t\t:")

  TAHUN_LAHIR = int(input("Tahun Lahir\t\t:"))
  BULAN_LAHIR = int(input("Bulan Lahir(1-12)\t:"))
  TANGGAL_LAHIR = int(input("Tanggal Lahir(1-31)\t:"))
  absen['Tanggal lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
  
  KEY = " ".join((random.choice(string.ascii_uppercase) for v in range(6)))
  data_baru.update({KEY:absen})
  
  print("\n")
  print(f"{'KEY':<15} {'NAMA':<20} {'KELAS':<15} {'UMUR':<15} {'TANGGAL LAHIR':<20}")
  print("-"*80)
  for absensi in data_baru:
    
    KEY = absensi
    
    NAMA = data_baru[KEY] ['Nama']
    KELAS = data_baru[KEY]['Kelas']
    UMUR = data_baru[KEY]['Umur']
    TANGGAL_LAHIR = data_baru[KEY]['Tanggal lahir'].strftime("%x")
    
    print(f"{KEY:<15} {NAMA:<20} {KELAS:<15} {UMUR:<15} {TANGGAL_LAHIR:<20}")
  
  print("\n")
  close = input("apakah ingin lanjut(y/n):")
  if close == "n":
      break
  print("THANK YOU END PROGRAM")