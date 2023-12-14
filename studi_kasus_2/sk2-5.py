list_menu = ["Pahe A", "Pahe B", "Parit A", "Parit B", "Box A", "Box B", "Big Bag 1", "Big Bag 2", "Burger", "Spaghetti", "Es Teh", "Lemon Tea"]

def cariMenu(list_menu, menu):
    for i in range(len(list_menu)):
        if list_menu[i] == menu:
            return i
    return -1

menu = input("Cari menu: ")
hasil = cariMenu(list_menu, menu)

if (hasil != -1):
    print(f"Menu {menu} tersedia, silahkan memesan")
else:
    print(f"Maaf, menu {menu} tidak tersedia")