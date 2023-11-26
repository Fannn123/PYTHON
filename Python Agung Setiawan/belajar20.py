#DICTIONARY
user = {
    "name": "irfan hafizzurohman",
    "age": 18,
    "is_admin": True
}

user["house"] = "rumah" # untuk menambahkan sebuah q baru
temp = user.get("house", "imahbsdgsdfg")
#None (sebuah tipe data yg menggambarkan sesuatu itu tidak ada)

print(temp)
 