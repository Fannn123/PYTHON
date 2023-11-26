#MENULIS FILE
users = open("users.txt_1", "w")#untuk mode "w"(write) jika filenya belum ada makan python secara otomatis akan langsung membuatnya

print(users.write("cupuk - dek"))
users.close