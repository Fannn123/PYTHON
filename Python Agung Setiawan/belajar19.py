#UNPEX
#UNPEX INI TIDAK HAYA DI TUPLE TETAPI DI LIST JUGA BISA

numbers = (1,2,3)

# x = numbers[0]
# y = numbers[1]
# z = numbers[2]

x, y, z = numbers
print(x) # x, y, z

X, _, _ = numbers #DI PYTHON JIKA KITA TIDAK INGIN MENGGUNAKAMN VARIABELNYA MAKA MENGGUNAKAN TANDA ANDESKOR (_)
print(x) #cuma bisa x karena variabel y dan z di abaikan  menggunakan (_)

x , *a = numbers #untuk 1 disimpan di variabel (x), untuk (*a) disini adalah untuk memasukan nilai 2 dan 3 
print(x)
print(a)