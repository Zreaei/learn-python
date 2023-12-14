array = []
elemen = int(input("Masukan jumlah elemen: "))

for i in range(0, elemen):
    angka = int(input("Masukan angka: "))
    array.append(angka)

def sorting(array):
    angka = len(array)
    for i in range(angka):
        for j in range(angka - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def arraySearch(array, cari):
    low, high = 0, len(array) - 1

    while low <= high:
        middle = (low + high) // 2
        midValue = array[middle]

        if midValue == cari:
            return middle
        elif midValue < cari:
            low = middle + 1
        else:
            high = middle - 1
    return -1

cariAngka = int(input("Masukan angka yang ingin dicari: "))
sortedArray = sorting(array)
hasil = arraySearch(sortedArray, cariAngka)

if (hasil != -1):
    print(f"\nAngka {cariAngka} ditemukan pada index ke-{hasil}")
else:
    print("Maaf, nilai yang dicari tidak ada dalam array.")