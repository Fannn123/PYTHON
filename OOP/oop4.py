# membuat method 

class umum:
    
    def __init__(self,name,email,pasword):
        #instace variable
        self.nama = name
        self.email = email
        self.kata_sandi = pasword
    
    #method tanpa argumen
    def fungsi(self):
        return f"{self.nama} - {self.email} - {self.kata_sandi}"    
    
    #method dengan argumen
    #bihefier -> tidak bisa asal mengganti namanya
    def uppdate_nama(self,up):
        if self.nama != "irfan hafizzurohman":
             self.nama = up
        
    
object1 = umum("irfan hafizzurohman", "fannn123@gmail.com", 25022005)
object2 = umum("gusti nugroho", "gustir@gmail.com", 3072004)


print(object1.fungsi())
object1.uppdate_nama("deden supriyeden")
print(object1.fungsi())
print('\n')
print(object2.fungsi())
object2.uppdate_nama("cucu cece cici")
print(object2.fungsi())