# Belajar method return value

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")
    return (list_angka, total)


list_angka, total = jumlahkan(10, 10, 10, 10, 40)

# Mengambil data total
print(f"Total {list_angka} = {total}")