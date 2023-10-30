# Studi Kasus 4
"""Arsya mempunyai lemari es yang penuh dengan buah-buahan. Di dalam
lemari es milik arsya terdapat 3 buah apel, 2 buah jeruk, 2 buah nanas, 1
buah durian, dan 1 buah alpukat. Setelah beberapa minggu, semua buah
apel, jeruk, dan alpukat busuk sehingga harus dikeluarkan dari lemari es.
Bantulah Arsya dalam membuat program python untuk mencari tahu sisa
buah yang ada di lemari es!"""

# Jawab
list_awal = input("Masukkan list awal: ").replace(" ", "").split(",")
list_filter = input("Masukkan list filter: ").replace(" ", "").split(",")

list_hasil = list_awal.copy()
for item_awal in list_awal:
    for item_filter in list_filter:
        if item_awal == item_filter:
            list_hasil.remove(item_filter)

print("Sisa:", list_hasil)