# - Syntax print()
print("Hello World")
print("Ohayo Sekai, Good Morning World")

# - print() dengan operator aritmatika
print("Helo" * 2)

# - Aritmatika sederhana dengan print()
print(19+3)
print(32-45)
print(3*3)
print(20/5)

# - Syntax Comment (ini adalah comment)
print("Comment tidak akan dieksekusi")

# - Multiline Comment
# Contohnya
# Seperti
# Ini

print("atau")

"""Seperti
Ini"""

# - Variable (untuk menyimpan data yang dapat berubah)
a = "Hello"
print(a)

b = 20
print(b)

# Penamaan variabel yang dapat dilakukan
namavariabel = "Hello"
namaVariabel = "Hello"
NamaVariabel = "Hello"
_namavariabel = "Hello"
nama_variabel = "Hello"
namavariabel2 = "Hello"

# Casting variable (menentukan tipe datanya)
a = int(3)
b = float(3)
c = str(3)

# a adalah integer
print(a)
print(type(a))

# b adalah float
print(b)
print(type(b))

# c adalah string
print(c)
print(type(c))

# Multiwords variable
# Snake case
nama_variabel_pertama = "Hello"

# Camel case
namaVariabelPertama = "Hello"

# Pascal case
NamaVariabelPertama = "Hello"

# Multi assign variable
a, b, c = "apel", "durian", "nangka"
print(a)
print(b)
print(c)

a = b = c = "apel"
print(a)
print(b)
print(c)

# Output variable
a = "Ohayo"
b = "Sekai"
c = "Good Morning"
d = "World"
print(a, b, c, d)

a = "SelamatPagi"
b = "Dunia"
c = "GoodMorning"
d = "World"
print(a + b + c + d)

x = 2
y = 9
print(x + y)

# Output
a = 30
print("Nilai anda sekarang adalah", a)

a = 10
b = 30
print("Nilai a adalah {0} dan nilai b adalah {1}".format(a, b))

a = 49
b = 11
print(f"Nilai a adalah {a} dan nilai b adalah {b}")

# Input (memberikan masukan saat program berjalan)
nama = input("Masukan nama anda : ")
print(f"Nama anda adalah {nama}")
print(f"Selamat datang, {nama}")

# Input dengan typecasting
umur = int(input("Masukan umur anda : "))
print(f"Umur anda adalah {umur}")
print(type(umur))

# Tipe Data di Python
# String
a = "Halo"
print(type(a))
# Integer
a = 2
print(type(a))
# Float
a = 2.5
print(type(a))
# Complex
a = 2j
print(type(a))
# List
a = ["Apel", "Nanas", "Durian"]
print(type(a))
# Tuple
a = ("Apel", "Nanas", "Durian")
print(type(a))
# Dictionary
a = {"Buah" : "Apel", "Jumlah" : 2}
print(type(a))
# Sets
a = {"Apel", "Belimbing", "Cherry"}
print(type(a))
# Boolean
a = True
print(type(a))

# Fungsi Tipe Data Numeric
# Absolute(x) - Mengembalikan nilai absolute dari suatu nilai x
a = abs(-10)
print(a)
# Max(x1,x2,x3) - Mengembalikan nilai paling besar dari seluruh nilai m
a = max(1,3,5)
print(a)
# Min(x1,x2,x3) - Mengembalikan nilai paling kecil dari seluruh nilai
a = min(1,3,5)
print(a)
# Pow(x,y) - Mengembalikan nilai x ** y
a = pow(2,3)
print(a)
# Round(x,a) - Membulatkan nilai x sejumlah nilai a dibelakang koma
a = round(10.7273,2)
print(a)

# Fungsi Tipe Data String
# Len - mengecek panjang dari sebuah strings
a = "Hello World"
print(len(a))

# Multiline Strings
a = """ini 
adalah multiline
strings"""
print(a)

# Slicing Strings (Index dimulai dari 0)
a = "Halo, Selamat Pagi"
print(a[0:4])
print(a[:5])
print(a[10:])

# Modifikasi String
a = "Hello World"
# Upper - mengubah string menjadi huruf kapital
print(a.upper())
# Lower - mengubah string menjadi huruf kecil
print(a.lower())
# Strip - menghapus spasi sebelum/setelah teks sesungguhnya (whitespace)
print(a.strip())
# Replace - mengganti suatu karakter dengan karakter lain dalam string
print(a.replace("H", "J"))
# Split - mengembalikan string menjadi list di antara karakter pemisah tertentu
print(a.split(","))

# Strings Concatenation - menggabungkan dua buah strings atau lebih dengan menggunakan operator tambah “+”
a = "Bahasa"
b = "Pemrograman"
c = "Python"
print(a + b + c)
print(a + " " + b + " " + c)

# Strings Formatting - fungsi format() digunakan untuk menggabungkan string dan number di Python
umur = 20
text = "Nama saya zam umur saya {}"
print(text.format(umur))

# {}
jumlah = 4
harga = 5000
uang = 20000
order = "Saya beli {} buah apel yang harganya Rp. {} dengan uang Rp. {}"
print(order.format(jumlah, harga, uang))

# {index}
jumlah = 4
harga = 5000
uang = 20000
order = "Saya beli {0} buah apel yang harganya Rp. {1} dengan uang Rp. {2}"
print(order.format(jumlah, harga, uang))

# f
jumlah = 4
harga = 5000
uang = 20000 
print(f"Saya beli {jumlah} buah apel yang harganya Rp. {harga} dengan uang Rp. {uang}")
