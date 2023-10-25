data = {
    'manggo' : 'mangga',
    'orange' : 'jeruk',
    'apple'  : 'apel',
    'banana' : 'pisang'
}

for kamus in data:
    print(f"{kamus}\n")
    
#    
key = data.keys()
print(f"{key}")
#
for key in data.keys():
    print(f"{data.get(key)}\n")
    
#
values = data.values()
print(values)
#
for value in data.values():
    print(f"{value}\n")
   
#   
item = data.items()
print(f"{item}")
#
for item in data.items():
    print(f"{item}\n")
#
for key,values in data.items(): #method items, untuk mengambil dua-duanya
    print(f"inggris:{key}, indonesia:{values}")  

    
    
    
