#TYPE CONVERSION
Year = input("tahun lahirmu adalah : ")
Year = int(Year)
Age = 2023 - Year
print("umur kamu adalah : " + str(Age))

#MENCARI TAU TIPE VARIABEL DENGAN FUNGSION type()
Year = input("tahun lahirmu adalah : ")
print(type(Year))

Year = int(Year)
print(type(Year))

Age = 2023 - Year
print("umur kamu adalah : " + str(Age))