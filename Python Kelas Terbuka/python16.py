#width and multiline

#data
data_nama = "irfan"
data_umur = 18
data_tinggi = 175.5
data_sepatu = 45

#string standard
data_str = f"nama: {data_nama}, umur: {data_umur}, tinggi: {data_tinggi}, sepatu: {data_sepatu}"
print(5*"="+"DATA STRING"+"="*5)
print(data_str)

#string multiline dengan(dengan menggunakan enter, newline, \n)
data_str = f"nama: {data_nama}, \numur: {data_umur}, \ntinggi: {data_tinggi}, \nsepatu: {data_sepatu}"
print("\n"+5*"="+"DATA STRING"+"="*5)
print(data_str)

# string multiline (kutip triplets)
data_str = F"""nama:{data_nama}
umur:{data_umur}
tinggi:{data_tinggi}
sepatu:{data_sepatu}
"""
print("\n"+5*"="+"DATA STRING"+"="*5)
print(data_str)

#mengatur lebar
data_nama = "keyla"
data_str = F"""
nama  :{data_nama:>10}
umur  :{data_umur:>10}
tinggi:{data_tinggi:>10}
sepatu:{data_sepatu:>10}
"""
print("\n"+5*"="+"DATA STRING"+"="*5)
print(data_str)