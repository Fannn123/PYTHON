#latihan

print(10*"-"+"KALKULATOR"+"-"*10+"\n")

angka_1 = float(input("masukkan angka: "))
operator = input("OPERATOR(+, -, *, /):")
angka_2 = float(input("masukan angka : "))

if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah: {hasil}")
elif operator == "-" :
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah: {hasil}")
elif operator == "*" :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah: {hasil}")
elif operator == "/" :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah: {hasil}")
else:
    print("WRONG: silahkan masukan lagi!!!")
print("END PROGRAM")    
