#staticmethod and classmethod untuk class variable

class Mooton:
    #private class variable
    __jumlah = 0
    
    def __init__(self,name):
        self.__name = name
        Mooton.__jumlah += 1
        
    #method ini hanya berlaku untuk object
    def get_jumalah(self):
        return Mooton.__jumlah
    
    
    #hanya berlaku untuk class 
    #tidak berlaku untuk object
    def get_jumlah1():
        return Mooton.__jumlah    
    
    #method static (decorator) menempel pada objek dan class
    @staticmethod
    def get_jumlah2(): # -> sama seperti class method, tetepi static method tidak menggunakan parameter
        return Mooton.__jumlah
    
    
    @classmethod
    def get_jumlah3(parameter): # ->sedangkan class method menggunakan parameter(dengan nama bebas)
        return parameter.__jumlah
    
fanny = Mooton('fanny')
print(fanny.get_jumlah2())
karri = Mooton('karri')
print(karri.get_jumlah2())
balmoon = Mooton('balmoon')
print(balmoon.get_jumlah3())



# print(fanny.get_jumalah())
# print(Mooton.get_jumlah1())
