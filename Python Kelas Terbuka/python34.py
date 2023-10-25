#program list buku

data_list = []
while True :
  judul = input("Masukan judul buku?\t")
  penulis = input("Masukan penulis?\t")

  buku_buku = [judul,penulis]
  data_list.append(buku_buku)


  for index,buku in enumerate(data_list):
      print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    
  user = input("Apakah mau melanjutkan?(y/n)")

  if user == "n":
    break
    
print("END PROGRAM")
