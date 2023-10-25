#menggunakan encapsulasi bawaan python
#getter
#setter

class Pb:
    
    def __init__(self,name,blood,attack):
        self.name = name
        self.__blood = blood
        self.__attack = attack
        
        
    @property
    def blood(self):
        pass
    
    @blood.getter
    def blood(self):
      return self.__blood
    
    @blood.setter
    def blood(self,user):
      self.__blood = user
      
    @blood.deleter
    def blood(self):
      self.__blood = None
    
    
wizart = Pb("wizart",50,100)

print("membuat getter dan setter dengan __blood")
print(wizart.blood)
print(wizart.__dict__)
wizart.blood = 100
print(wizart.blood)
print('\n')

del wizart.blood
print(wizart.blood)
print(wizart.__dict__)