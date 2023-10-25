#operasi logika atau boolean
#not, or, and, xor
"""
 TABEL KEBENARAN
 =====NOT=====
 -NOT TRUE = FALSE
 -NOT FALSE = TRUE 
 =====OR=====
 -FALSE OR TRUE = TRUE
 -TRUE OR FALSE = TRUE
 -FALSE OR FALSE = FALSE
 -TRUE OR TRUE = TRUE
 =====AND=====
 -FALSE AND TRUE = FALSE
 -TRUE AND FALSE = FALSE
 -FALSE AND FALSE = FALSE
 -TRUE AND TRUE = TRUE
 =====XOR=====
 -FALSE XOR TRUE = TRUE
 -TRUE XOR FALSE = TRUE
 -FALSE XOR FALSE = FALSE
 -TRUE XOR TRUE = FALSE
"""

print("=====NOT=====")
a = True
b =False
c =  not b
print("hasilnya adalah : ", c)

print("=====OR=====")
a = True
b =False
c = a or b
print("hasilnya adalah : ", c)

print("=====AND=====")
a = True
b =False
c = a and b
print("hasilnya adalah : ", c)

print("=====XOR=====")
a = True
b = True
c = a ^ b
print("hasilnya adalah : ", c)