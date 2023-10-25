#encapsulasi biasa
#menjaga supaya instace variable tidak bisa diubah sembarangan

class Mooton:
    
    def __init__(self,name,attack,blood):
        self.__name = name
        self.__attack = attack
        self.__blood = blood
       
    #getter -> tidak bisa diubah
    def get_name(self):
        return self.__name
    
    def get_blood(self):
        return self.__blood    
    
    def get_attack(self):
        return self.__attack   
    
    #setter -> untuk merubah
    def attack_lawan(self,user):
        self.__blood -= user
       
    def setup(self,heal):
         self.__blood += heal
        
    
yzhoung = Mooton("yzhoung",500,1000)



print(yzhoung.get_name())
yzhoung.get_name = "paquito"
print(yzhoung.get_name)
print(yzhoung.__dict__)

# print(yzhoung.__dict__)
# yzhoung.attack_lawan(200)
# print(yzhoung.get_blood())
# print(yzhoung.__dict__)

# print(yzhoung.__dict__)
# yzhoung.get_name = "karina"
# print(yzhoung.get_name)
# print(yzhoung.__dict__)
