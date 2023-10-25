class Oop:
    
    def __init__(self ,name:str ,tall:int ,heavy:int):
        self.name = name
        self.__tall = tall
        self.__heavy = heavy
     
    def info(self):
        return f"{self.name} - {self.__tall} - {self.__heavy}"
    
        
    @property    
    def tall(self):
         pass 
    @tall.getter 
    def tall(self):
        return self.__tall   
    @tall.setter
    def tall(self,input_user):
        self.__tall = input_user
       
        
    @property
    def heavy(self):
       pass
    @heavy.getter
    def heavy(self):
         return self.__heavy
    @heavy.setter
    def heavy(self,input_user):
        self.__heavy = input_user        
        
        
azis = Oop("abdul azis", 168, 55)
    
print(azis.__dict__) 

print("\ncontoh normal")  
print(azis.name)
print(azis.tall)
print(azis.heavy)
print('\n')

print(azis.__dict__) 
azis.name = "defry"
print(azis.name)
azis.heavy = 50
print(azis.tall)
azis.tall = 165
print(azis.heavy)
print(azis.info())
print(azis.__dict__) 