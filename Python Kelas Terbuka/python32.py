data0 = [1,2]
data1 = [3,4]
data_gabungan = [data0,data1,10]
data_copy = data_gabungan.copy()

print(F"data gabungan\t\t={data_gabungan}")
print(F"data copy\t\t={data_copy}")

#ambil data dari neted list
data = data_gabungan[0] [0]
print(F"data yg diambil\t\t={data} ")
print("\n"+20*"-"+"\n")

#addres semuanya
print(f"data asli(gabungan)\t={hex(id(data_gabungan))}")
print(f"data copy(copy)\t\t={hex(id(data_copy))}")
print("\n"+20*"-"+"\n")

print('"addres dari data ke-1"')
print(f"data asli(gabungan)\t={hex(id(data_gabungan[0]))}")
print(f"data copy(copy)\t\t={hex(id(data_copy[0]))}")
print("\n"+20*"-"+"\n")

data_gabungan[1][0] = 5
data_gabungan[2] = 9
print(F"data gabungan\t\t={data_gabungan}")
print(F"data copy\t\t={data_copy}")
print("\n"+20*"-"+"\n")

#kita gunakan deep copy
from copy import deepcopy
 
data_gabungan = [data0,data1,10]
data_deepcopy = deepcopy(data_gabungan)

print(F"data gabungan\t\t={data_gabungan}")
print(F"data deepcopy\t\t={data_deepcopy}")
print("\n"+20*"-"+"\n")

print('"addres dari data ke-1"')
print(f"data asli(gabungan)\t={hex(id(data_gabungan[0]))}")
print(f"data deepcopy(copy)\t={hex(id(data_deepcopy[0]))}")
print("\n"+20*"-"+"\n")

data_gabungan[1][0] = 30
print(F"data gabungan\t\t={data_gabungan}")
print(F"data copy\t\t={data_copy}")
print(F"data deepcopy\t\t={data_deepcopy[1]}")