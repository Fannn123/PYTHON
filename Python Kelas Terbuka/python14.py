#operator dalam bentuk method

##merubah case dari string

#merubah semua ke upper case
name = "hallo world"
name = name.upper()
print(name)

komande = "".center(31,"=")
print("'"+komande+"'")

#merubah semua ke lower case
name = "MAKAn naSI uduK"
name = name.lower()
print(name)

komande = "".center(31,"=")
print("'"+komande+"'")


#pengecekan dengan isX method

#contoh pengecekan lower case
nama = "Kesya" #jika salah satunya huruf besar makan akan bernilai false
nama = nama.islower() #hasilnya adalah bool
print("hailnya case lower:" + str(nama))
nama = "ZAKI" #jika salah satunya huruf kecil makan akan bernilai false
nama = nama.isupper() #hasilnya adalah bool
print("hailnya case upper:" + str(nama))

komande = "".center(31,"=")
print("'"+komande+"'")


#isalpha() <-- untuk mengecek semuanya huruf
#isalnum() <-- huruf dan angka
#isdecimal() <-- angaka saja
#isspace() <-- space, tab dan newline \n
#istitle() <-- semua kata diawali dengan huruf besar 

#istitle
name = "zuned Bin Syayem" #setiap kata harus diawali dengan huruf besar kalau tidak akan menghasilkan nilai true
name = name.istitle()
print("hasil istitle: " + str(name))

komande = "".center(31,"=")
print("'"+komande+"'")


#pengecekan dengan startswith() endswith()
starts_with = "bilal bin rabbah".startswith("bilal") #jika yang dimasukan bukan kata awal maka nilainya akan false
print("starts:" + str(starts_with))
ends_with = "bilal bin rabbah".endswith("rabbah") #jika yang dimasukan bukan kata akhir maka nilainya akan false
print("end:" + str(ends_with))

komande = "".center(31,"=")
print("'"+komande+"'")


##penggabungan komponen join() split()
names = ['sakura', 'hinata', 'tsunade'] 
names = "{ }".join(names) # -> sebagai pengganti koma
print(names)

name = ("sakura{ }hinata{ }tsunade")
print(name.split("{ }"))

komande = "".center(31,"=")
print("'"+komande+"'")

#alokasi karakter rjust() ljust() center()

komande = "BATAS".rjust(10)#dimulai dari saf(10) dari kanan dan di akhiri ke saf(1)dikiri
print("-"+komande+"-")
komande = "BATAS".ljust(10)
print("+"+komande+"+")
komande = "BATAS".center(21,"=")
print("|"+komande+"|")

komande = "".center(31,"=")
print("'"+komande+"'")


#kebalikannya --> strip()
komande = "BATAS".strip("=")#UNTUK MENGHAPUS KARAKTER SAMADENGAN(=) YG DIPAKAI DI CENTER
print(" "+komande+" ")
