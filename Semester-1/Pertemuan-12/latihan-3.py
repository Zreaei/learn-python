# Nama : Muhammad Rafi Zamzami
# NIM : 2301678
# Kelas : 1A-RPL

from time import perf_counter
import numpy as np

"""Dari algoritma Linear Search dan Binary Search yang telah Anda pelajari, buatlah perbandingan
running program (execution time) dengan 2 algoritma tersebut. Buatlah dengan menggunakan
sortedArray berikut : array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]
Tentukan manakah dari ke 2 algoritma tersebut yang paling cepat untuk mencari nilai 60?"""

sortedArray = np.array([1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100])

# Linear/Sequential Search
def linearSearch(array, nilai):
    for i in range(len(array)):
        if array[i] == nilai:
            return i
    return -1
    
nilai = 60
t_start = perf_counter()
result = linearSearch(sortedArray, nilai)
t_end = perf_counter()

print("\nLinear/Sequential Search: ")
print(f"\nTime Start : {t_start}")
print(f"Time End : {t_end}")
print(f"Time Elapsed : {((t_end-t_start) * 1000):.3}\n")

# Binary Search
def binarySearch(arr, cariNilai):
    indexLow, indexHigh = 0, len(arr) - 1

    while indexLow <= indexHigh:
        middle = (indexLow + indexHigh) // 2
        middleValue = arr[middle]

        if middleValue == cariNilai:
            return middle
        elif middleValue < cariNilai:
            indexLow = middle + 1
        else:
            indexHigh = middle - 1
    return -1

cariAngka = 60
time_start = perf_counter()
hasil = binarySearch(sortedArray, cariAngka)
time_end = perf_counter()

print("\nBinary Search: ")
print(f"\nTime Start : {time_start}")
print(f"Time End : {time_end}")
print(f"Time Elapsed : {((time_end-time_start) * 1000):.3}\n")