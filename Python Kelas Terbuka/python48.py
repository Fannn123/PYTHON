'''*ARGS'''

#memasukan data/argument
def fungsi(nama,kelas,umur):
    print(f"nama saya {nama} dan saya kelas {kelas} umur saya {umur}")
    
fungsi('herik','13 TOI 2','19 tahun')
print('\n')

def data(data_list):
    data = data_list.copy()
    nama = data[0]
    kelas = data[1]
    umur = data[2]
    print(f"nama saya {nama} dan saya kelas {kelas} umur saya {umur}")
   
data(['zaki','12 TOI 2','19 tahun'])

#menggunakan *args
def data_args(*args):
    nama = args[0]
    kelas = args[1]
    umur = args[2]
    print(f"nama saya {nama} dan saya kelas {kelas} umur saya {umur}")
   
data_args('suyuf',13,19) 

def tambah(*data):
    output = 0
    for x in data:
        output += x
        
    return output

hasil = tambah(5,10,15)
print(f"haasilnya = {hasil}")        
 
hasil = tambah(10,20,30,40,50)
print(f"haasilnya = {hasil}")        
 