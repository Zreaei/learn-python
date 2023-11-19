"""Seorang guru Matematika memiliki data nilai ujian sebanyak 30 orang. Guru tersebut ingin
menyimpan seluruh nilai ujian tadi ke dalam sebuah array untuk kemudian diurutkan
nilainya dari yang terbesar hingga terkecil, kemudian ditampilkan. Selain itu, guru tersebut
ingin melihat 5 nilai terbesarnya saja. Buatlah programnya dengan menggunakan library
Numpy! (Catatan: silahkan buat data dummy untuk nilai ujian 30 siswa tersebut).
"""

# Nama : Muhammad Rafi Zamzami
# NIM : 2301678
# Kelas : 1A-RPL

import numpy as np

def random_array(low: int, high: int, size: int):
    rng = np.random.default_rng()
    return rng.integers(low=low, high=high, size=size)

nilai_ujian = random_array(0, 100, 30)
nilai_ujian.sort()
nilai_terurut = nilai_ujian[::-1]

print(f"Nilai Ujian Setelah Diurutkan: ")
print(nilai_terurut)
print(f"\nMenampilkan 5 Nilai Ujian: ")
print(nilai_terurut[:5])
