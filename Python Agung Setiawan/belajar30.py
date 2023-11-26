#WITH BLOCK
#DI PYTHON LEBIH DIREKOMENDASIKAN JIKA MEMBUKA FILE MENNGUNAKAN WITH BLOCK
import csv

with open("users.csv", "r") as users:#jika terjadi eror di pertengahan secara otomatis program akan di tutup
    users_csv = csv.reader(users, delimiter=",")
    
    for a in users_csv:
        print(f"Name : {a[0]}. Nick_Name : {a[1]}. Role : {a[2]}")