# Nama : Muhammad Rafi Zamzami
# NIM : 2301678
# Kelas : 1A-RPL

"""Sebuah toko memiliki stok barang yang tersedia. Buatlah program Python untuk mencari apakah
suatu barang tersedia dalam stok toko.. (Buatlah array dummy dimana jumlah elemen ada 15 barang)
"""

def cariBarang(list_barang, barang):
    for i in range(len(list_barang)):
        if list_barang[i] == barang:
            return i
    return -1
    
list_barang = ["Mouse", "Handphone", "Earphone", "Joystick", "Laptop", "Keyboard", "Charger", "Mousepad", "Flashdisk", "Kamera", "Monitor", "VGA", "Motherboard", "RAM", "SSD"]
barang = "Handphone"
result = cariBarang(list_barang, barang)

if (result != -1):
    print(f"{barang} ditemukan pada index ke-{result}")
else:
    print(f"{barang} tidak ditemukan dalam array!")
