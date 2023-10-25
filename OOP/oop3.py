# instace variable and class variable

class people:
    #class variable
    jumlah = 0
    
    def __init__(self,name,age,):
        #instace variable
        self.name = name
        self.age = age
        people.jumlah += 1
        print(f"nama saya {self.name} umur saya {self.age}") 

object1 = people("irfan hafizzurohman", 18)
print(people.jumlah)        
object2 = people("zaki hudani", 19)
print(people.jumlah)              