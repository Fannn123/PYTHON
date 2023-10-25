class dota:
    
    def __init__(self,name,blood,attack) -> None:
        self.name = name
        self.__blood = blood
        self.__attack = attack
        # self.__info = "name: {} \n\t blood: {}".format(self.name,self.__blood) 
        
    def fungsi(self):
        return f"{self.name} - {self.__blood} - {self.__attack}"
    
    def getter_blood(self): # -> ketika diubah hanya akan berubah diluar class, sedangkan didalam class nilainya akan sama seperti semula
        return self.__blood
    
    # def getter_name(self):
    #     return self.__name
    
    @property # -> untuk memanggil(method) seperti variabel, dan nilainya dapat berubah-ubah
    def info(self):
        return "name: {} \n\t blood: {} \n\t attack: {} ".format(self.name,self.__blood,self.__attack) 

keli = dota('keli',100,30)


# print(keli.info)
# keli.name = "maxim" # -> kalau seperti ini ia akan mengganti nilai yg didalam class dan juga diluar class
# print(keli.info)
# print(keli.fungsi())
# print(keli.__dict__)


# keli.name = "joyjo" # -. kalau seperti ini bisa juga sama seperti memakai @property

print(keli.fungsi())

keli.getter_blood = 500 # -> kalau kasusnya seperti ini dia hanya akan berubah diluar classnya saja sedangkan didalam classnya nilainya akan sama seperti semula dan ketika di print akan membuat intace baru
print(keli.getter_blood)

print(keli.fungsi())
print(keli.__dict__)


