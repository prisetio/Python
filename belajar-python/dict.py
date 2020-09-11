# Belajar tipe data Dictionary

#customer = ("Priyo", 27, "Cianjur")

customer = {"Name":"Priyo", "Age":27, "Address":"Cianjur"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "X"
customer["Name"] = "Priyo Setio"

del customer["Address"]

for key, value in customer.items():
     print(f"{key}:{value}")