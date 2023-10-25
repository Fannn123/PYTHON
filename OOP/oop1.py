#membuat class
class TOI2:
    pass


absen1 = TOI2() #object / instace(instansiate)
absen2 = TOI2()
absen3 = TOI2()

absen1.nama = "abdul azis"
absen1.NO_absen = 1

absen2.nama = "adira perdana irawan"
absen2.NO_absen = 2

absen1.nama = "gonary anggarda"
absen1.NO_absen = 15

print(absen1) #untuk mencari tau apakah ini object dari (TOI2) dan juga untuk mencari tau addresnya

print(absen1.__dict__) #untuk mencari tahu ada apa saja didalam object (abesen1)

print(absen1.nama) #untuk mencari tau ada apa saja didalam (absen1.nama)

print(absen1.NO_absen) #untuk mencari tau ada apa saja didalam obeject(absen1.NO_absen)


