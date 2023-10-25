#operasi bitwise, operasi biner, binary
a = 9
b = 5

#bitwise OR (|)
c = a | b
print("\n=====OR=====\n")
print("hasilnya: ",a, "binernya :", format(a,'08b'))
print("hasilnya: ",b, "binernya :", format(b,'08b'))
print("------------------------------------------")
print("hasilnya:", c,"binernya :", format(c,'08b'))


# #bitwise AND (&)
c = a & b
print("\n=====AND=====\n")
print("hasilnya: ",a, "binernya :", format(a,'08b'))
print("hasilnya: ",b, "binernya :", format(b,'08b'))
print("------------------------------------------")
print("hasilnya:", c,"binernya :", format(c,'08b'))


# #bitwise XOR (^)
c = a ^ b
print("\n=====XOR=====\n")
print("hasilnya: ",a, "binernya :", format(a,'08b'))
print("hasilnya: ",b, "binernya :", format(b,'08b'))
print("------------------------------------------")
print("hasilnya:", c,"binernya :", format(c,'08b'))


# #bitwise NOT (~)
c = ~a
print("\n=====NOT=====\n")
print("hasilnya: ",a, "binernya :", format(a,'08b'))
print("------------------------------------------")
print("hasilnya:",c,"binernya:", format(c,'08b'))
print("------------------------------------------")
d = 0b0000001001
e = 0b1111111111
print("hasilnya:", e^d,"binernya :", format(e^d,'08b'))


# shifting
#shift right (>>)
c = a >> 2
print("\n=====>>=====\n")
print("hasilnya: ",a, "binernya :", format(a,'08b'))
print("------------------------------------------")
print("hasilnya:",c,"binernya:", format(c,'08b'))

#shift left (<<)
c = a << 2
print("\n=====<<=====\n")
print("hasilnya: ",a, "binernya :", format(a,'08b'))
print("------------------------------------------")
print("hasilnya:",c,"binernya :", format(c,'08b'))


