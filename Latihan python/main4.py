import random


#("\u25cf,\u250c,\u2500,\u2510,\u2502,\u2514,\u2518")

#   ●   ┌   ─   ┐   │   └    ┘

# ┌───────────┐
# │           │
# │           │
# │           │
# │           │
# │           │
# └───────────┘


dice_art = {1 : ("┌───────────┐",
                 "│           │",
                 "│           │",
                 "│     ●     │",
                 "│           │",
                 "│           │",
                 "└───────────┘"), 
            
           2  : ("┌───────────┐",
                 "│ ●         │",
                 "│           │",
                 "│           │",
                 "│           │",
                 "│         ● │",
                 "└───────────┘"), 
            
            
            3 : ("┌───────────┐",
                 "│ ●         │",
                 "│           │",
                 "│     ●     │",
                 "│           │",
                 "│         ● │",
                 "└───────────┘"), 
            
            4 : ("┌───────────┐",
                 "│  ●     ●  │",
                 "│           │",
                 "│           │",
                 "│           │",
                 "│  ●     ●  │",
                 "└───────────┘"), 
            
            5 : ("┌───────────┐",
                 "│  ●     ●  │",
                 "│           │",
                 "│     ●     │",
                 "│           │",
                 "│  ●     ●  │",
                 "└───────────┘"), 
            
           
            6 : ("┌───────────┐",
                 "│  ●     ●  │",
                 "│           │",
                 "│  ●     ●  │",
                 "│           │",
                 "│  ●     ●  │",
                 "└───────────┘"), 
             }

dice = []
total = 0
number_dice = int(input("how many to dice: "))


for dic in range(number_dice):
   dice.append(random.randint(1, 6))
    
# result vertical
# for loop in range(number_dice):
#      for line in dice_art.get(dice[loop]):
#       print(line)

# result horizontal
for line in range(7): # -> untuk mengulang setiap baris
     for dic in dice:
        print(dice_art.get(dic)[line], end="")
     print()
  
     
for dic in dice:
     total += dic   
print(f"TOTAL: {total}")     