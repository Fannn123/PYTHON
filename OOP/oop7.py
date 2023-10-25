#private and protected

class Ml:
    #class variable
    jumlah = 0
    
    def __init__(self,name,attack,blood):
        #intance variable
        self.name = name
        self.attack = attack
        self.blood = blood
        
        #variable intance private
        self.__private = "private"
        
        #variable intance protected
        self._protected = "protected"
    
paquito = Ml("paquito", 500, 1200)

print(paquito.__dict__)

paquito._protected = 'new'
print(paquito.__dict__)
print(paquito._protected)

# paquito.__private = 'new'
# print(paquito.__dict__)
# print(paquito.__private)