# Studi Kasus 3
"""Arya sedang menyusun kalimat, tetapi dosen Pendidikan Bahasa
Indonesianya melarang Arya untuk menggunakan kata yang lebih dari 10
huruf. Bantulah Arya dalam mencari tahu kata mana yang lebih dari 10
dengan menggunakan program python!
"""

# Jawaban
kalimat = input("Masukan kalimat : ")
batas_huruf = int(input("Masukan batas huruf : "))
kata_lebih = []
kata = kalimat.split()
for i in range (0, len(kata)):
    if (len(kata[i]) > batas_huruf):
        kata_lebih.append(kata[i])
print(kata_lebih)