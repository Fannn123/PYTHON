#operasi aritmatika

a = 10
b = 3
c = 4
d = 5
e = 7

#operasi penjumlahan + 
hasil = a + b
print(a, "+", b, "hasilnya : ", hasil)

#operasi pengurangan - 
hasil = a - b
print(a, "-", b, "hasilnya : ", hasil)

#operasi perkaloian *
hasil = a * b
print(a, "*", b, "hasilnya : ", hasil)

#operasi pembagian / 
hasil = a / b
print(a, "/", b, "hasilnya : ", hasil)

#operasi eksponen (pangkat) ** 
hasil = a ** b
print(a, "**", b, "hasilnya : ", hasil)

#operasi modulus (pembagian sisa) % 
hasil = a % b
print(a, "%", b, "hasilnya : ", hasil)

#operasi floor division (pembagian sisa) //
hasil = a // b
print(a, "//", b, "hasilnya : ", hasil)

#prioritas operasi
"""
 1. ()
 2. eksponen **
 3. perkalian dan kawan-kawan % / * // **
 4. penjumalahan dan pengurangan + -
"""
hasil = a + ( b * c ) / d ** e

print("hasilnya : ", hasil)