import datetime
data = {
    'Nama':"aaaaaa",
    'Kelas':'13 TOI 2',
    'Umur':'19 tahun',
    'Tanggal lahir': datetime.datetime(1111,1,11)
}

data_baru = {}

print(f"{'ABSENSI TO CLASS 13 TOI 2':<20}")
print("-"*30)

absen = dict.fromkeys(data.keys())

absen['Nama'] = input("Nama(Siswa/Siswi)\t:")
absen['Kelas'] = input("Kelas\t\t\t:")
absen['Umur'] = input("Umur\t\t\t:")

TAHUN_LAHIR = int(input("Tahun Lahir\t\t:"))
BULAN_LAHIR = int(input("Bulan Lahir(1-12)\t:"))
TANGGAL_LAHIR = int(input("Tanggal Lahir(1-31)\t:"))
print("\n")

absen['Tanggal lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(absen)
