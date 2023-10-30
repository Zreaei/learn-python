# Set - digunakan untuk menyimpan beberapa item dalam suatu variable (immutable, unordered, unindexed dan tidak ada duplikasi)
a = {"apel", "jeruk", "ceri", "durian"}
print(a)

# Bisa terdiri dari beberapa tipe data yang berbeda
a = {"apel", "jeruk", "ceri", "durian", True, 10}
print(a)

# Untuk mengakses item dalam set harus menggunakan loop/pengkondisian, karen set tidak memiliki index
setA = {"apel", "jeruk", "ceri", "durian"}
for item in setA:
    print(item)

# Menambah item pada set
a = {"apel", "jeruk", "ceri", "durian"}
a.add("semangka")
print(a)

# Menambah item di set dari set lainnya
a = {"apel", "jeruk", "ceri", "durian"}
b = {"strawberry", "blueberry"}
a.update(b)
print(a)

# Menambahkan dua buah set menggunakan union() - diperlukan deklarasi variabel baru
a = {"apel", "jeruk", "ceri", "durian"}
b = {"strawberry", "blueberry"}
c = a.union(b)
print(c)

# Mencari item yang sama dari dua buah set
a = {"apel", "jeruk", "ceri", "durian"}
b = {"strawberry", "blueberry", "apel", "jeruk"}
a.intersection_update(b)
print(a)

# Mencari item yang sama dari dua buah set - diperlukan deklarasi variabel baru
a = {"apel", "jeruk", "ceri", "durian"}
b = {"strawberry", "blueberry", "apel", "jeruk"}
c = a.intersection(b)
print(c)

# Mencari item yang berbeda dari dua buah set
a = {"apel", "jeruk", "ceri", "durian"}
b = {"strawberry", "blueberry", "apel", "jeruk"}
a.symmetric_difference_update(b)
print(a)

# Mencari item yang berbeda dari dua buah set - diperlukan deklarasi variabel baru
a = {"apel", "jeruk", "ceri", "durian"}
b = {"strawberry", "blueberry", "apel", "jeruk"}
c = a.symmetric_difference(b)
print(c)

# Menambah item di set dari sebuah list
a = {"apel", "jeruk", "ceri", "durian"}
b = ["strawberry", "blueberry"]
a.update(b)
print(a)

# Menambah item di set dari sebuah tuple
a = {"apel", "jeruk", "ceri", "durian"}
b = ("strawberry", "blueberry")
a.update(b)
print(a)

# Dictionary - digunakan untuk menyimpan data dengan format key: value, bersifat ordered (setelah Python v3.6), changeable, dan no duplication
kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
} 

print(kucing)

# Membuat dictionary baru dengan method dict()
buah = dict(nama = "Apel", warna = "Merah", manis = True)
print(buah)

# Mengakses item pada dictionary menggunakan nama key
kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
}

print(kucing["nama"])

# Mengakses item pada dictionary menggunakan method get()
kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
} 

print(kucing.get("ras"))

# Mengambil seluruh keys dari dictionary
kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
} 

print(kucing.keys())

# Mengambil seluruh values dari dictionary
kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
}

print(kucing.values())

# Update values dan menambahkan keys pada dictionary
kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
} 

print(kucing)
kucing["umur"] = 1.5
kucing["lucu"] = True
print(kucing)

# Update values dan menambah item dengan menggunakan method update()
kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
} 

kucing.update({"umur": "3"})
kucing.update({"warna": ["Hitam", "Putih"]})
print(kucing)

# Mengubah item pada dictionary menjadi sebuah tuple dalam list menggunakan method items() dan mengecek apakah terdapat suatu key dalam dictionary
kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
} 

x = kucing.items()
print(x)

if "nama" in kucing:
    print("Ada key 'nama' pada dictionary")

# Menghapus item pada dictionary menggunakan method pop()
kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
} 

kucing.pop("jantan")
print(kucing)
