import datetime
import os

absen1 = {
    'Nama' : 'Abdul Azis',
    'Kelas' : '13 TOI 2',
    'Umur' : '20',
    'Tanggal lahir' : datetime.datetime(2004,9,22)
}
absen2 = {
    'Nama' : 'Adira p.I',
    'Kelas' : '13 TOI 2',
    'Umur' : '19',
    'Tanggal lahir' : datetime.datetime(2005,1,12)
}
absen3 = {
    'Nama' : 'Yusuf T',
    'Kelas' : '13 TOI 2',
    'Umur' : '21',
    'Tanggal lahir' : datetime.datetime(2003,5,13)
}

absen_siswa = {
    'MURID1':absen1,
    'MURID2':absen2,
    'MURID3':absen3
}

os.system("cls")
print(f"{'NAMA':<13} {'KELAS':<10} {'UMUR':<8} {'TANGGAL LAHIR':<20}")
print("-"*60)


for absensi in absen_siswa:
    
    ABSEN = absensi
    
    NAMA = absen_siswa[ABSEN] ['Nama']
    KELAS = absen_siswa[ABSEN]['Kelas']
    UMUR = absen_siswa[ABSEN]['Umur']
    TANGGAL_LAHIR = absen_siswa[ABSEN]['Tanggal lahir'].strftime("%x")
    
    print(f"{NAMA:<13} {KELAS:<10} {UMUR:<8} {TANGGAL_LAHIR:<20}")