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