# For
jumlah_perulangan = 3
for index in range(jumlah_perulangan):
    print(f"Halo gais {index + 1}")

for i in "Python":
    print(f"Huruf {i}")

for i in range(1, 6):
    print(i)

buah = ["Apel", "belimbing", "cherry", "durian"]
for i in buah:
    print(f"Buah ke {i}")

buah = ["Apel", "belimbing", "cherry", "durian"]
for i in range(len(buah)):
    print(f"Buah {buah[i]}")

# While
angka = 0
while(angka <= 8):
    print(f"Angka sekarang: {angka}")
    angka += 1

# Break
angka = [1, 2, 3, 4, 5]
for i in angka:
    print(i)
    if i == 3:
        break

# Continue
angka = [1, 2, 3, 4, 5]
for i in angka:
    if i == 3:
        continue
    print(i)

# Ascending Range (2 = nilai awal, 6 = nilai akhir, 3 = kelipatan)
for i in range (2, 6, 3):
    print(i)

# Descending Range
for i in range (0, 105, 5):
    print(i)

# Nested Loop
buah = ["Apel", "Belimbing", "Cherry"]
angka = [1, 2]

for i in buah:
    for j in angka:
        print(j)
        print(i)

# Typedata Loops
list = ["apel", "anggur","mangga", "jeruk", "melon"]
# tanpa range
for item in list:
    print(item) 