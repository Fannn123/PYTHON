#
           
#index =  0/(-3)   1/(-2)     2/(-1)
data = ["gusti", "bodong", "sukriyadi"]

#
data_0 = data[0]
print(f"indeks 0 = {data_0}")
#
data_1 = data[1]
print(f"indeks 1 = {data_1}")
#
data_1 = data[-1]
print(f"indeks -1 = {data_1}")
print("\n---------------------------------\n")

# mengambil info jumlah data dalam list
data_name = len(data)
print(data_name)
print("\n---------------------------------\n")


## manipulasi data pada list

#menambah item pada list sesuai posisi
data.insert(1, "arhan")
print(f"data insert = {data} ")
print("\n---------------------------------\n")

#menambah diakhir list
data.append("jajang")
print(f"data append = {data} ")
print("\n---------------------------------\n")

#menambah list dengan list
data_baru = ["yudi", "sahrul", "zaki"]
data.extend(data_baru)
print(f"data gabungan = {data} ")
print("\n---------------------------------\n")

#merubah data 
#kita ubah data 2 menjadi "puji"
data[2] = "puji"
print(f"data baru = {data} ")
print("\n---------------------------------\n")

# data remove
data.remove("jajang")
print(f"data remove = {data} ")
print("\n---------------------------------\n")

#data append
data_pop = data.pop()
print(f"data akhir= {data_pop} ")



