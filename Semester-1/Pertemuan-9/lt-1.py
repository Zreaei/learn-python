"""Buatlah Program untuk menampilkan Deret Fibonacci dengan menggunakan fungsi"""
def deretFibonacci(panjang_deret):
    n1, n2 = 0, 1
    total = 0

    for i in range(panjang_deret):
        print(total)
        n1, n2 = n2, total
        total = n1 + n2

input_deret = int(input(f"Masukan panjang deret: "))
deretFibonacci(input_deret)