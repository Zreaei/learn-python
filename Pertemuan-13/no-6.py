list_siswa = []
jml_siswa = int(input("Masukan jumlah siswa: "))

for i in range(0, jml_siswa):
    siswa = input("Masukan nama siswa: ")
    nilai = int(input("Masukan nilai siswa: "))
    list_siswa.append({"nama": siswa, "nilai": nilai})

def sortNilai(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j]["nilai"] < array[j + 1]["nilai"]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def cariSiswa(list_siswa, cari_siswa):
    for i in range(len(list_siswa)):
        if list_siswa[i]["nama"] == cari_siswa:
            return i
    return -1

cari_siswa = input("Cari siswa: ")
peringkat = sortNilai(list_siswa)
hasil = cariSiswa(list_siswa, cari_siswa)

if (hasil < 3):
    print(f"Nama Siswa: {peringkat[hasil]}, Peringkat: {hasil + 1}")
else:
    print(f"{peringkat[hasil]} masih harus belajar dengan giat")


