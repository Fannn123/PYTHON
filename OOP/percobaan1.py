# ilustrasi serang menyerang dalam game mobile legends

class ML:
    
    def __init__(self,name,attack,critical,blood):
        self.name = name
        self.attack = attack
        self.blood = blood
        self.critical = critical
    
    def serang(self,musuh):
        print(self.name + " menyerang " + musuh.name )
        musuh.diserang(self)
        
    def diserang(self,lawan):
        print(self.name + " diserang " + lawan.name) 
        damage_diterima = self.attack + self.critical
        print("dengan damage yg diterima : "+ str(damage_diterima))
        sisah_darah = self.blood - damage_diterima
        print("HP : "+ str(sisah_darah)) 
     
     
        
objek1 = ML("balmoon",30,650,1200)
objek2 = ML("fanny",25,600,1100)


objek1.serang(objek2) 
print('\n')
objek2.serang(objek1)

    