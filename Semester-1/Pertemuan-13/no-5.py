list_menu = ["Ayam Gulai", "Babat", "Cumi", "Ikan Kembung", "Kikil", "Limpa", "Otak", "Paru", "Rendang", "Telur", "Usus"]

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