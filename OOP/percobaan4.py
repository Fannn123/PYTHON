class Ml:
    #private class variable
    __jumlah = 0
    
    def __init__(self,name,health,attack,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attackStandar = attack
        self.__armorStandar = armor
        self.__level = 1
        self.__uppgrade = 0
        
        self.__healthMAX = self.__healthStandar * self.__level
        self.__attack = self.__attackStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        
        self.__health = self.__healthStandar
        
        
    @property
    def info(self):
        return '{} level {}: \n\t health: {}/{} \n\t attack: {} \n\t armor: {} \n\t'.format(self.__name,self.__level,self.__health,self.__healthMAX,self.__attack,self.__armor)
    
    
    @property
    def UPPDATE(self):
        pass
    
    @UPPDATE.setter
    def UPPDATE(self, input_user):
        self.__uppgrade += input_user
        if(self.__uppgrade >= 100):
            print(self.__name + "Level Up!")
            self.__level +=1
            self.__uppgrade -= 100
            
        self.__healthMAX = self.__healthStandar * self.__level
        self.__attack = self.__attackStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
            
    
    
    def serang(self,musuh):
        self.UPPDATE = 50
    
      
    
    
karina = Ml("karina",100,10,5)
harrit = Ml("harrit",100,10,5)



karina.serang(harrit)
karina.serang(harrit)
karina.serang(harrit)
print(karina.info)
print(karina.__dict__)


                