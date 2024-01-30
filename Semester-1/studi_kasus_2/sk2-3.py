input_array = []
jml_elemen = int(input("Masukan jumlah elemen: "))

for i in range(0, jml_elemen):
    jml_angka = int(input("Masukan angka: "))
    input_array.append(jml_angka)

def sorting(array):
    angka = len(array)
    for i in range(angka):
        for j in range(angka - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

print(f"\nHasil Sorting dari {jml_elemen} angka diatas adalah")
print(sorting(input_array))