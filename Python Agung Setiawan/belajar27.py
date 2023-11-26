# MEMBACA FILE
users = open("users.txt", "r")
print(users.read())
users.close()
#mode:
#"r"/read (untuk mwmbaca sebuah file)
#"w"/write (untuk menulis data kesebuah file baru dan file yg lamanya akan terhapus)
#"a"/append (untuk menambah baris/elem baru dan akan ditaro dipaling akhir)
#"r+" (untuk membaca dan menulis)