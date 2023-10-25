#private attribute

class jtk:
    
    def __init__(self,name,email,paspord):
        self.nama = name
        self.__email = email # <- menggunakan private attribute
        self.kata_sandi = paspord
        
    def perulangan(self):
        return f"{self.nama} - {self.__email} - {self.kata_sandi}" # <- private hanya bisa diakses ketika berada didalam class
    
    def perubahan(self,ganti):
        if self.__email != "zakihudn@yahoo.com":
            self.__email = ganti
            


obejek1 = jtk("zaki hudani","zakihudn@yahoo.com",23566149)
print(obejek1.perulangan())
obejek1.perubahan("dadfn@13yhoo.com")

obejek1.__email = "zkt4@gmail.com"
print(obejek1.perulangan())