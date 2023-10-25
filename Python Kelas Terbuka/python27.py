# list
# kumpulan data
numbers = [1,2,3,4,5]
print(numbers,"\n")

# kumpulan data string
names= ["irfan", "udin", "saski"]
print(names, "\n")

# kumpulan data boolean
bool = [True, False]
print(bool, "\n")

# kumpulan data campuran
campuran = [1, "yusuf", True, False]
print(campuran, "\n")

# cara alternatif membuat list
data_range = range(0,10,2) # range (start,stop,step)
data_list = list(data_range)
print(data_list, "\n")

# membuat list dengan for loop, list comprehension
list_for = [i for i in range(0,10)] #cara baca: {DIDALAM LIST SAYA MENARUH (i), DIMANA i UNTUK i DIDALAM (range)}
print(list_for, "\n")

# membuat list dengan for dan if
list_forif = [i for i in range(0,10) if i != 5]
print(list_forif)

list_forif = [i for i in range(0,10) if i%2 == 0]
print(list_forif)

list_forif = [i for i in range(0,10) if i%2 != 0]
print(list_forif)