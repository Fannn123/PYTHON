#(+ - * / EXIT)
command = "" #SEBAGAI KALIMAT PERINTAH 
 
while command != "exit" :
    command = input("perintah : ") #PERINTAHNYA UNTUK (+ - * /) 
    
    if command == "exit" :
        break
    
    if command != "+" and  command != "-" and command != "*" and command != "/" :
        print("erorrrrrr!!!!!")
        continue #tidak akan dilanjut ke bawah jika perintah diatas salah
    
    a = int(input("angka pertama : "))
    b = int(input("angka ke-dua : "))
    
    if command == "+" :
        jawaban = a + b
    elif command == "-" :
        jawaban = a - b
    elif command == "*" :
        jawaban = a * b
    elif command == "/" :
        jawaban = a / b
        
    print(f"hasilnya : {jawaban}")
            


print("terimaksih telah bermain")