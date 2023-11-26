#MEMBACA CSV (COMMA SEPARATED VALUES)

import csv #SEBELUM MEMBUAT MODEUL HARUS MENGIMPORT SEBUAH MODUL

users = open("users.csv", "r")

users_csv = csv.reader(users, delimiter=",")#UNTUK MEMCARI MODUL CSV MENGUNAKAN METHODE.reader
#DELIMITER (UNTUK MENGETAHUI PEMBATAS KOLOM TERSEBUT MENGGUNAKAN APA)
for a in users_csv:
    print(F"Name : {a[0]}. Nick_Name : {a[1]}. Role : {a[2]}")
    
users.close()