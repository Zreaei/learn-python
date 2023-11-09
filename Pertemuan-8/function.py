# Function
def penjumlahan(a, b):
    hasil = a + b
    return hasil

print(penjumlahan(10, 5))

# Procedure
def greeting(nama):
    print(f"Selamat datang {nama}")

greeting("Andi")

def greeting2():
    nama = input(f"Masukan nama anda : ")
    print(f"Selamat datang {nama}")

greeting2()

# Global Var
globalVar = 10

def globalFunction():
    print(f"Nilai dari global variabel adalah {globalVar}")

globalFunction()
print(globalVar)

# Local Variabel
def lokalFunction():
    lokalVar = 5
    print(f"Nilai dari lokal var adalah {lokalVar}")
    
# print(lokalVar) akan menimbulkan error
lokalFunction()

# Parameter dengan input
def greeting2(nama):
    print(f"Selamat datang {nama}")

greeting2(input(f"Masukan nama anda : "))

# Default Value
def greeting(nama = "Zam"):
    print(f"Selamat datang {nama}")

greeting()
greeting("Andi")
greeting("Andika")

# Keyword Arguments
def penjumlahan(a, b):
    print(f"Hasilnya adalah {a - b}")

penjumlahan(b = 9, a = 7)
penjumlahan(9, 7)

# Arbitrary Arguments
def funcArgs(*angka):
    print(f"Angka terakhir yang dimasukan yaitu {angka[-1]}")

funcArgs(1, 2, 3, 4, 5)

# Arbitrary Keyword Arguments
def funcArgs(**angka):
    print(f"Angka terakhir yang dimasukan yaitu {angka['ketiga']}")

funcArgs(pertama = 1, kedua = 2, ketiga = 3, keempat = 4, kelima = 5)

# Arguments from List
def namaBuah(buah):
    for i in buah:
        print(i)

buah = ["Apel","Jeruk","Mangga","Anggur"]
namaBuah(buah)

# Pass (untuk menghindari error apabila function belum selesai dibuat)
def kosong():
    pass