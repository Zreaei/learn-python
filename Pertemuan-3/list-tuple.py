# Tipe Data Sequence dalam python merupakan tipe data yang terorganisir, yang setiap elemennya ditandai dengan angka (index) yang diawali dengan 0

# List - mutable, ordered dan duplikasi
a = ["apel", "jeruk", "ceri", "durian", "apel"]
print(len(a))

# Mengambil item berdasarkan index
print(a[2])

# Mengambil item berdasarkan range tertentu
print(a[1:4])

# Menambah item diakhir list
a.append("sirsak")
print(a)

# Mengganti item tertentu
a[2] = "manggis"
print(a)

# Menambah item di range tertentu
a.insert(3, "semangka")
print(a)

# Menghapus item di index tertentu
a.pop(3)
print(a)

# List dengan tipe data berbeda
a = ["apel", "jeruk", "ceri", "durian", "apel", True, 10]
print(a)

# Menambah item di list dari list lainnya
a = ["apel", "jeruk", "ceri", "durian"]
b = ["blueberry", "strawberry"]

# Sebelum di extend
print(a)
# Setelah di extend
a.extend(b)
print(a)

# Mengurutkan item sesuai abjad
# Sebelum di sort
print(a) 
# Setelah di sort
a.sort()
print(a)

# Method pada list
# clear() - Menghapus semua item di list
# copy() - Menyalin list
# count() - Menghitung jumlah item tertentu di pada list
# extend() - Menambah item dari list lain ke dalam list tersebut
# index() - Menampilkan index dari suatu item tertentu pada list
# remove() - Menghapus item tertentu pada list
# reverse() - Membalikkan susunan item pada list
# sort() - Mengurutkan susunan item berdasarkan alfabet

# Tuple - immutable, ordered dan duplikasi
a = ("apel", "jeruk", "ceri", "durian", "apel")
print(len(a))

# Mengambil item tertentu
print(a[3])

# Mengambil item pada range tertentu
print(a[1:4])

# Karena bersifat immutable (tidak dapat berubah), kita perlu merubahnya ke list apabila ingin memodifikasi tuple
a = ("apel", "jeruk", "ceri", "durian", "apel")
x = list(a)
x[3] = "melon"
a = tuple(x)
print(a)

# Manipulasi data untuk menambah item
a = ("apel", "jeruk", "ceri", "durian", "apel")
x = list(a)
x.insert(1, "melon")
a = tuple(x)
print(a)

# Manipulasi data untuk menghapus item
a = ("apel", "jeruk", "ceri", "durian", "apel")
x = list(a)
x.pop(2)
a = tuple(x)
print(a)

# Manipulasi data untuk menambah item diakhir
a = ("apel", "jeruk", "ceri", "durian", "apel")
x = list(a)
x.append("mangga")
a = tuple(x)
print(a)

# Tuple dapat menyimpan data dengan tipe data berbeda
a = ("apel", "jeruk", "ceri", "durian", "apel", True, 10)
print(a)

# Packing
buah = ("apel", "jeruk", "ceri", "durian", "mangga")
# Unpacking
(a, b, c, d, e) = buah
print(a)
print(b)
print(c)
print(d)
print(e)