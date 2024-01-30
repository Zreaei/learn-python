"""Seorang ilmuan memiliki sebuah array 1D yang isinya adalah suhu di Singapura selama 10
hari terakhir. Suhu tersebut ingin dikonversi dari Celcius menjadi Farenheit. Buatlah
programnya dengan menggunakan library Numpy! (Catatan: silahkan buat data dummy
untuk suhu 10 hari tersebut)."""

# Nama : Muhammad Rafi Zamzami
# NIM : 2301678
# Kelas : 1A-RPL

import numpy as np

# Hard Code Dummy
arr = np.array([24, 26, 22, 27, 26, 23, 24, 28, 27, 28])

def convert(celcius):
    return 9/5 * celcius + 32

print(f"Suhu singapura 10 hari terakhir dalam celcius: {arr} ")
print(f"Suhu singapura 10 hari terakhir dalam fahrenheit: {convert(arr)}")

# # Generated Dummy
# def random_array(low: int, high: int, size: int):
#     rng = np.random.default_rng()
#     return rng.integers(low=low, high=high, size=size)

# def convert(celcius):
#     return 9/5 * celcius + 32

# suhu_singapura = random_array(-100, 100, 10)

# print(f"Suhu singapura 10 hari terakhir dalam celcius: {suhu_singapura} ")
# print(f"Suhu singapura 10 hari terakhir dalam fahrenheit: {convert(suhu_singapura)}")