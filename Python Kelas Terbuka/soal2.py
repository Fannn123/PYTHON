## soal 1

user = float(input("masukan angka?"))
print("\n")

## memerikasa angka lebih dari 0
# -----0+++++
lebih_dari_nol = user > 0
print(f"lebih dari 0: {lebih_dari_nol}")
## memeriksa angka kurang dari nol
# +++++5-----
kurang_dari_lima = user < 5
print(f"kurang dari 5: {kurang_dari_lima}")

#-----0+++++5-----
hasil_lima_nol =lebih_dari_nol and kurang_dari_lima
print(f"hasil dari 0 and 5 = {hasil_lima_nol}")
print("------------------------------\n")


## memeriksa angak lebih dari delapan
# -----8+++++
lebih_dari_delapan = user > 8
print(f"lebih dari 8: {lebih_dari_delapan}")
## memeriksa kurang dari sebelas
# +++++11-----
kurang_dari_sebelas = user < 11
print(f"kurang dari 11: {kurang_dari_sebelas}")

#-----8+++++11-----
hasil_delpan_sebelas = lebih_dari_delapan and kurang_dari_sebelas
print(f"hasil dari 8 and 11 = {hasil_delpan_sebelas}")
print("------------------------------\n")


## penggabungan
# -----0+++++5-----8+++++11-----
gabungan =hasil_lima_nol or hasil_delpan_sebelas
print(f"hasil dari gabungan adalah = {gabungan}")
print("------------------------------\n")
user = float(input("masukan angka?"))
print("\n")



# ## soal 2

# user = float(input("masukan angka?"))
# print("\n")

# ## memerikasa angka kurang dari 0
# # +++++0-----
# kurang_dari_nol = user < 0
# print(f"lebih dari 0: {kurang_dari_nol}")
# ## memeriksa angka lebih dari nol
# # -----5+++++
# lebih_dari_lima = user > 5
# print(f"kurang dari 5: {lebih_dari_lima}")

# # +++++0-----5+++++
# hasil_lima_nol =kurang_dari_nol or lebih_dari_lima
# print(f"hasil dari 0 or 5 = {hasil_lima_nol}")
# print("------------------------------\n")



# ## memeriksa angak lebih dari delapan
# # +++++8-----
# kurang_dari_delapan = user < 8
# print(f"lebih dari 8: {kurang_dari_delapan}")
# ## memeriksa kurang dari sebelas
# # +++++11-----
# lebih_dari_sebelas = user > 11
# print(f"kurang dari 11: {lebih_dari_sebelas}")

# # +++++8-----11+++++
# hasil_delpan_sebelas = kurang_dari_delapan or lebih_dari_sebelas
# print(f"hasil dari 8 and 11 = {hasil_delpan_sebelas}")
# print("------------------------------\n")



# ## penggabungan
# # +++++0-----5+++++8-----11+++++
# gabungan =hasil_lima_nol and hasil_delpan_sebelas
# print(f"hasil dari gabungan adalah = {gabungan}")
# print("------------------------------\n")
