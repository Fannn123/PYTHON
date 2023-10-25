# format string

#contoh generic

#string
name = "sizuka"
format_str = f"my name is: {name}"
print(format_str)
print("-------------------------")

#boolean
bool = True
format_str = f"nilainya bool: {bool}"
print(format_str)
print("-------------------------")

#angka
angka = 2005.5
format_str = f"nilainya angka: {angka}"
print(format_str)
print("-------------------------")

#bilangan bulat
angka = 15
format_str = f"nilainya bilangan bulat: {angka:d}"
print(format_str)
print("-------------------------")

#angka dengan ordo ribuan
angka = 200000
format_str = f"nilainya adalah: {angka:,}"
print(format_str)
print("-------------------------")

# angka desimal
angka = 2005.4567
format_str = f"nilainya desimal: {angka:.2f}"
print(format_str)
print("-------------------------")

# menampilkan leading zero
angka = 2005.5467
format_str = f"nilainya desimal: {angka:010.3f}" #menambahkan 
print(format_str)
print("-------------------------")

# menampilkan tanda + dan -
angka_minus = -10
angka_plus = 10.2345
format_minus = f"nilai minus: {angka_minus}"
format_plus = f"nilai plus: {angka_plus:+.2f}"
print(format_minus)
print(format_plus)
print("-------------------------")

# memformat persen
angka = 0.045
format_persen = f"nilai persen: {angka:.2%}"
print(format_persen)
print("-------------------------")

#melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
format_str = f"harga total adalah: Rp. {harga*jumlah:,}"
print(format_str)
print("-------------------------")

# format angka lain(binary, hexadesimal, octal)
angka = 255
format_bin = f"nilai binary: {bin(angka)}"
format_hex = f"nilai hexa: {hex(angka)}"
format_oct = f"nilai octal: {oct(angka)}"
print(format_bin)
print(format_hex)
print(format_oct)

