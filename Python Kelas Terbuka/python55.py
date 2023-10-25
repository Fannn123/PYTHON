import datetime

data_waktu = datetime.datetime.now()
print(f"data waktu : {data_waktu}")
print(f"thun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")

from collections import Counter

kumpulan_data = ['1','1','7','9','5','4','8','7']
data = Counter(kumpulan_data)
print(f"data counter : {data}") #akan menghasilkan dictionary
# untuk mengaambil key nya
print(f"data counter 1 : {data['1']}")
