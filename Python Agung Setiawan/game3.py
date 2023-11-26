user = input("silahkan cari disini :")

numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "thre",
    "4": "four",
    "5": "vive",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}    
output = ""    
for a in user:
    temp = numbers.get(a, "invalid")
    output = output + temp + " "
print(output)