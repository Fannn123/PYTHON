print("""
                       ----------------------------
                       |     LOMBA 17 AGUSTUS     |
                       |       HUT RI KE-78       |
                       ----------------------------
      
      
      
                        LOMBA MAKAN KERUPUK ANAK SD
           ---------------------------------------------------------            
           |   NO   |  PESERTA LK  |   UMUR   |  TINGGI  |  KELAS  |
           --------------------------------------------------------- 
           |   1    | ARYA         | 11 TAHUN |  150 CM  |  6 SD   | 
           |   2    | EPAN         | 12 TAHUN |  145 CM  |  5 SD   |
           |   3    | PIYEL        | 10 TAHUN |  155 CM  |  6 SD   |
           |   4    | MIRJA        | 10 TAHUN |  150 CM  |  6 SD   |
           |   5    | BEBI         | 12 TAHUN |  140 CM  |  5 SD   |
           |   6    | GUNTUR       | 11 TAHUN |  150 CM  |  4 SD   |
           |   7    | DERIL        | 11 TAHUN |  155 CM  |  4 SD   |
           
           
           --------------------------------------------------------
           |  NO   |  PESERTA PR  |   UMUR   |  TINGGI  |  KELAS  |  
           ------------------------------------ -------------------
           |   1   | RISKA        | 12 TAHUN |  150 CM  |  6 SD   |
           |   2   | ABEL         | 11 TAHUN |  140 CM  |  5 SD   |
           |   3   | AYU          | 11 TAHUN |  145 CM  |  6 SD   |
           |   4   | ENCIM        | 11 TAHUN |  145 CM  |  5 SD   |
           |   5   | WULAN        | 11 TAHUN |  150 CM  |  5 SD   |
           |   6   | AMIRA        | 10 TAHUN |  140 CM  |  6 SD   |
           |   7   | CUNENG       | 10 TAHUN |  150 CM  |  5 SD   |           
""")
print("\n NAMA PESERTA LOMBA MAKAN KURUPUK:")


nama_peserta = ["ARYA", "EPAN", "PIYEL", "MIRJA", "BEBI", "GUNTUR", "DERIL","RISKA" ,"ABEL", "AYU", "ENCIM", "WULAN", "AMIRA", "CUNENG"]
print(f" NAMA PESERTA : {nama_peserta}")

umur_peserta = [11,12,10,]
tinggi_peserta = ["140 CM", "145 CM", "150 CM", "155 CM"]
kelas = ["6 SD", "5 SD", "4 SD"]

import random 
nilai = 0
while nilai < 5:
  user= input("\nSIAPAKAH PESERTA YG AKAN BERLOMBA\t:")
  if user == "ACAK":
      undi = random.choice(nama_peserta)
      print(f"PESERTA YG DIPILIH: {undi}")
  
  #peserta laki-laki
  # 1
  if undi == "ARYA":
      print(f"NAMA\t: {nama_peserta[0]} \nUMUR\t: {umur_peserta[0]} TAHUN \nTINGGI\t: {tinggi_peserta[2]} \nKELAS\t: {kelas[0]}\n")
  # 2
  elif undi == "EPAN":
      print(f"NAMA\t: {nama_peserta[1]} \nUMUR\t: {umur_peserta[1]} TAHUN \nTINGGI\t: {tinggi_peserta[1]} \nKELAS\t: {kelas[1]}\n")
  # 3
  elif undi == "PIYEL":
      print(f"NAMA\t: {nama_peserta[2]} \nUMUR\t: {umur_peserta[2]} TAHUN \nTINGGI\t: {tinggi_peserta[3]} \nKELAS\t: {kelas[0]}\n")
  # 4
  elif undi == "MIRJA":
      print(f"NAMA\t: {nama_peserta[3]} \nUMUR\t: {umur_peserta[2]} TAHUN \nTINGGI\t: {tinggi_peserta[2]} \nKELAS\t: {kelas[0]}\n")
  # 5
  elif undi == "BEBI":
      print(f"NAMA\t: {nama_peserta[4]} \nUMUR\t: {umur_peserta[1]} TAHUN \nTINGGI\t: {tinggi_peserta[0]} \nKELAS\t: {kelas[1]}\n")
  # 6
  elif undi == "GUNTUR":
      print(f"NAMA\t: {nama_peserta[5]} \nUMUR\t: {umur_peserta[0]} TAHUN \nTINGGI\t: {tinggi_peserta[2]} \nKELAS\t: {kelas[2]}\n")
  # 7
  elif undi == "DERIL":
      print(f"NAMA\t: {nama_peserta[6]} \nUMUR\t: {umur_peserta[0]} TAHUN \nTINGGI\t: {tinggi_peserta[3]} \nKELAS\t: {kelas[2]}\n")
      
  
  #pesertas perempuan
  # 1
  elif undi == "RISKA":
      print(f"NAMA\t: {nama_peserta[7]} \nUMUR\t: {umur_peserta[1]} TAHUN \nTINGGI\t: {tinggi_peserta[2]} \nKELAS\t: {kelas[0]}\n")
  # 2
  elif undi == "ABEL":
      print(f"NAMA\t: {nama_peserta[8]} \nUMUR\t: {umur_peserta[0]} TAHUN \nTINGGI\t: {tinggi_peserta[0]} \nKELAS\t: {kelas[1]}\n")
  # 3
  elif undi == "AYU":
      print(f"NAMA\t: {nama_peserta[9]} \nUMUR\t: {umur_peserta[0]} TAHUN \nTINGGI\t: {tinggi_peserta[1]} \nKELAS\t: {kelas[0]}\n")
  # 4
  elif undi == "ENCIM":
      print(f"NAMA: {nama_peserta[10]} \nUMUR\t: {umur_peserta[0]} TAHUN \nTINGGI\t: {tinggi_peserta[1]} \nKELAS\t: {kelas[1]}\n")
  # 5
  elif undi == "WULAN":
      print(f"NAMA\t: {nama_peserta[11]} \nUMUR\t: {umur_peserta[0]} TAHUN \nTINGGI\t: {tinggi_peserta[2]} \nKELAS\t: {kelas[1]}\n")
  # 6
  elif undi == "AMIRA":
      print(f"NAMA\t: {nama_peserta[12]} \nUMUR\t: {umur_peserta[2]} TAHUN \nTINGGI\t: {tinggi_peserta[0]} \nKELAS\t: {kelas[0]}\n")
  # 7 
  elif undi == "CUNENG":
    print(f"NAMA\t: {nama_peserta[13]} \nUMUR\t: {umur_peserta[2]} TAHUN \nTINGGI\t: {tinggi_peserta[2]} \nKELAS\t: {kelas[1]}\n")
      
  
      
  nilai += 1
      
      
  if user != "ARYA" and user != "PIYEL" and user != "DERIL" and user != "MIRJA" and user != "BEBI" and user != "GUNTUR" and user != "EPAN" and user != "AYU" and user != "CUNENG" and user != "AMIRA"and user != "WULAN"and user != "ENCIM"and user != "RISKA"and user != "ABEL" and user != 'ACAK':
      print("NAMA TIDAK TERDAFTAR!!!!")
      continue
      
  else:
      if 5  < nilai :
          break
      
print("SILAHKAN KELAPANGAN UNTUK MENGIKUTI LOMBA MAKAN KERUPUK")
print("END PROGRAM ")      
