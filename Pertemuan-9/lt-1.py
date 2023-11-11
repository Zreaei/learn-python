"""Buatlah Program untuk menampilkan Deret Fibonacci dengan menggunakan fungsi"""
# Input nilai awal
def deretFibonacci(panjang_deret):
    np = nilai_pertama
    nk = nilai_kedua
    jml = 0
    
    for i in range(panjang_deret):
        print(jml)
        np, nk = nk, jml
        jml = np + nk

nilai_pertama = int(input(f"Masukan nilai pertama: "))
nilai_kedua = int(input(f"Masukan nilai kedua: "))
input_deret = int(input(f"Masukan banyak input: "))

deretFibonacci(input_deret)

# Tanpa input nilai awal
def deretFibonacci(panjang_deret):
    n1, n2 = 0, 1
    total = 0

    for i in range(panjang_deret):
        print(total)
        n1, n2 = n2, total
        total = n1 + n2

input_deret = int(input(f"Masukan panjang deret: "))
deretFibonacci(input_deret)