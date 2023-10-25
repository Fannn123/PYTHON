data = ("ini adalah string")
print(data)
print(type(data))
print("---------------")

#cara membuat string
"""
 1. menggunakan singel quot '...'
 2. menggunakan double quot "..."
"""

data = ('menggunakan singel quot')
print(data)
data = ("menggunakan double quot")
print(data)

print("'hallo world'")
print('"hallo world"')
print("hari jum'at")
print("---------------")

#menggunakan tanda \
    
#membuat tanda ' menjadi string
print('mari solat jum\'at')
print('i think we\'re ready')
print("---------------")

#backslash
print("user\\nick name\\Id")
print("---------------")

#tab
print("nama ku\t\t\tlahab")
print("---------------")

#backspace
print("nama \bku udin")
print("---------------")

#newline
print("user: irfan\nId: 21345")#lf-->line feed --->uni,macos,linux 
print("user: asep\rId: 3638643")#CR-->carriage return --->commodore,acorn,list
print("user: supra\r\nId: 234564")#CRLF-->carriage return line feed --->dipakai untuk windows
print("---------------")

# 3. string literal atau raw

#hati-hati
print('c:\new folder\\ini yang salah')#akan salah pahtnya
#meggunakan raw string (r)
print(r'c:\new folder\ini yang benar')
print("---------------")

#multiline literal string
print("""
 User : Mikasa
 Id   : 2341156
 Role : Jungler
""")
#multiline literal string dan raw
print(r"""
 Nama: asep s.
 Email: asep@.gmail.com
 Websait: www.googleducnk.com
 File: https\\suberterpercaya\\3242\\uyyy\\.com
""")
