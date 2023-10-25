'''TYPE HINTS PADA FUNGSI'''

def fungsi(argument:int) -> int:#untuk mencari tau type dari si argument,tetapi tidak akan berpengaruh pada saat dijalankan hanya untuk mengetahui typenya apa
    pangkat = 10**argument
    return pangkat
    
operasi = fungsi(2) #akan mengeluarkan hasil int jika menambahkan expression (-> int), ketika ingin mengeluarkan hasil yg lain maka akan terjadi eror 
print(operasi)
print('\n')


import string
def display(argument:string):
    print(argument)
    
display("usup")