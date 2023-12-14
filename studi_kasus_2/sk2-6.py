mhs = []
nilai_mhs = []
jml_mahasiswa = int(input("Masukan jumlah mahasiswa: "))

for i in range(0, jml_mahasiswa):
    mahasiswa = input("Masukan nama mahasiswa: ")
    nilai = int(input("Masukan nilai mahasiswa: "))
    mhs.append(mahasiswa)
    nilai_mhs.append(nilai)

def cariMahasiswa(mhs, mahasiswa):
    for i in range(len(mhs)):
        if mhs[i] == mahasiswa:
            return i
    return -1

def sortNilai(array):
    nilai = len(array)
    for i in range(nilai):
        for j in range(nilai - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

cari_mahasiswa = input("Cari mahasiswa: ")
peringkat = sortNilai(nilai_mhs)
hasil = cariMahasiswa(mhs, cari_mahasiswa)


