# MODUL MATEMATIKA

def OPS_tambah(*data1):
    output = 0
    for angka1 in data1:
        output += angka1
        return output


def OPS_kali(*data2):
    output = 1
    for angka2 in data2:
        output *= angka2
        return output
    
    
def OPS_pangkat(pangkat:int):
    return lambda angka : angka**pangkat
    
    