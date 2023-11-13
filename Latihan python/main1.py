import os

questions = ("Siapakah yang menjahit bendera merah putih? ",
             "Pada tahun berapa indonesia merdeka? ",
             "Apa itu DPR? ",
             "Apa Lambang Negara Indonesia?  ",
             "Apa lambang Partai PDI? ")

options = (("a. W.R Supratman","b. Ir Soekarno","c. Ganjar Pranowo","d. IBu Fatmawati"),
           ("a. 1945","b. 1953","c. 1845","d. 1873"),
           ("a. Dewan Perkorupsian Rakyat","b. Dewan penipu Rakyat","c. Dewan Perwakilan Rakyat","d. Dewan Pemimpin Rakyat"),
           ("a. Burung Cendrawasi","b. Burung bango ","c. Burung Garuda","d. Harimau"),
           ("a. Scorpion","b. Dragon","c. Banteng Hitam","d. Banteng"))


answers = ("D","A","C","C","D")
guesses = []
score = 0
parts_number = 0

os.system('cls')
for question in questions:
    print("-"*30)
    print(question)
    for option in options[parts_number]:
        print(option)
   
    print('\n')
    user = input("Enter (a,b,c,d): ").upper()
    guesses.append(user)
    
    if user == answers[parts_number]:
        score += 1
        print("CORRECT \n")
        
    else:
        print("INCORRECT")
        print(f"({answers[parts_number]}) is the answer \n")
        
    parts_number += 1
    
print("-"*30)
print(f"{'RESULT':^30}")
print("-"*30)

print("answers: ", end="")
for answer in answers:
     print(answer, end=" ")
print()
print("guess: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
    
score = (score / len(questions) * 100)
print(f"score: {score}")