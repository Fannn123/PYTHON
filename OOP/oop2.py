class user:
    
    def __init__(self,name,age,profil):
        self.nama = name
        self.umur = age
        self.status = profil
        
object_1 = user("sukriyadi",23,"belum menikah")
object_2 = user("imrom",30,"sudah menikah")

print(object_1.nama)
print(object_1.status)
print(object_2.nama)
print(object_2.status)