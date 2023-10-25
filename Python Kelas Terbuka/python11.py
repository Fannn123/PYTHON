#operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assignment
a = 5 #ini adalah assignment
b = 10
c = 15
d = 20
print("nilai a : ", a)
print("\n----------\n")

a += 1# artinya a = a + 1
print("nilainya a += 1 : ",a)
b -= 2# artinya a = a - 1
print("nilainya b -= 2 : ",b)
c *= 5# artinya a = a * 1
print("nilainya c *= 5 : ",c)
d /= 2# artinya a = a / 1
print("nilainya d /= 2 : ",d)

print("\n--------------------\n")

#modulus
s = 10
print("nilainya s : ",s)
s %= 3 
print("nilainya 10 %= 3 : ",s)
print("\n----------\n")
#floor division
g = 15
print("nilainya g : ",g)
g //= 3 
print("nilainya 15 //= 3 : ",g)
print("\n----------\n")
#eksponen
i = 5
print("nilainya i : ",i)
i **= 2 
print("nilainya 5 **= 2 : ",i)

print("\n--------------------\n")

#operasi bitwaise
#OR
z = True
print("nilai z :",z)
z |= False
print("z |= false :",z)
print("\n---------\n")

#AND
x = False
print("nilai x :",x)
x &= True
print("x &= true:",x)
print("\n----------\n")

#XOR
y = True 
print("nilainya y : ",y)
y ^= False
print("y ^= false : ",y)

v = True
print("nilainya v : ",v)
v ^= True
print("v ^= true : ",v)
print("\n----------------------\n")

#geser-geser
k = 0b0100
print("nilai k : ", format(k,'04b'))
print("\n----------\n")

#right
k >>= 2
print("nilai k >>= 2 :", format(k,'04b'))
#left
k <<= 1
print("nilai k <<= 1 :", format(k,'04b'))

