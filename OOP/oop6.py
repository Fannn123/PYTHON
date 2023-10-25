class Ml:
    
    def __init__(self,hero,attack,blood,armor):
        self.hero = hero
        self.attack = attack
        self.Hp = blood
        self.vest = armor
        
    def serang(self,musuh1):
        print(self.hero + " menyerang " + musuh1.hero)
        musuh1.diserang(self)
        
    def diserang(self,musuh2):
        print(self.hero + " diserang " + musuh2.hero)
        damage_diterima = self.attack/self.vest
        print("kerusakan yg diterima: " + str(damage_diterima))
        darah = self.Hp - damage_diterima
        print("darah tersisah: " + str(darah))

hero1 = Ml("Harit",500,1000,100)
hero2 = Ml("faramis",100,780,100)

hero1.serang(hero2)