## teknik menduplikasi list

a = ["sasa", "eka", "joko"]
print(f"hasil a = {a}")

b = a
print(f"hasil b = {b}")
print("\n"+15*"-"+"pembatas"+"-"*15+"\n")


#merubah member dari a
a[2] = "dudung"
b.sort()
print(f"hasil a = {a}") #a juga akan berubah ketika b berubah karena alamat addresnya sama
print(f"hasil b = {b}") #hasil b akan sama,karena b hanya mengambil nilai dari si a termasauk addresnya
print("\n"+15*"-"+"pembatas"+"-"*15+"\n")


# addres dari kedua lis a dan b 
print(f"hasil a = {hex(id(a))}")
print(f"hasil b = {hex(id(b))}") 
print("\n"+15*"-"+"pembatas"+"-"*15+"\n")

#menduplikat list dengan copy
c = a.copy() #membuat list yg baru dengan cara mengcopy nya dengan alamat addres yg berbeda

print(f"hasil a = {hex(id(a))}")
print(f"hasil b = {hex(id(b))}") 
print(f"hasil c = {hex(id(c))}") # alamat c akan berbeda dengan b malaupun keduanya mengambil nilai dari a
print("\n"+15*"-"+"pembatas"+"-"*15+"\n")


print(f"hasil a = {a}") #a juga akan berubah ketika b berubah karena alamat addresnya sama
print(f"hasil b = {b}") #hasil b akan sama,karena b hanya mengambil nilai dari si a termasauk addresnya
print(f"hasil c = {c}") 
print("\n"+15*"-"+"pembatas"+"-"*15+"\n")

""" 
1. b akan selau sama hasilnya dengan a, karena b hannya mengabil nilai list dari si a tetapi tidak dengan addresnya
2. nilai c akan berbeda dengan b walaupun keduanya sama-sama mengambil nilai dari a, tetapi c tidak mengambi nilainya saja melaikan bersama dengan addresnya
3. jadi semisal a diubah hanya b yg ikut berubah karena alamat addres a dan b sama
4. sedangankan c akan tetap sama karena addres yg dimiliki c berbeda dengan a dan juga b 
"""

c[2] = "fadli"

print(f"hasil a = {a}") #a juga akan berubah ketika b berubah karena alamat addresnya sama
print(f"hasil b = {b}") #hasil b akan sama,karena b hanya mengambil nilai dari si a termasauk addresnya
print(f"hasil c = {c}") 
print("\n"+15*"-"+"pembatas"+"-"*15+"\n")


a[2] = "yoga"

print(f"hasil a = {a}") #a juga akan berubah ketika b berubah karena alamat addresnya sama
print(f"hasil b = {b}") #hasil b akan sama,karena b hanya mengambil nilai dari si a termasauk addresnya
print(f"hasil c = {c}") 
