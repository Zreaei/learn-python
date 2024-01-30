# Nama : Muhammad Rafi Zamzami
# NIM : 2301678
# Kelas : 1A-RPL

"""Universitas Pendidikan Indonesia memiliki daftar mahasiswa yang terdaftar di prodi RPL. Buatlah
program Python untuk mencari apakah nama seorang mahasiswa tertentu ada dalam daftar
tersebut? (Buat nama tersebut berdasarkan inputan dari user dan buat array dummy 20 elemen untuk
daftar nama mahasiswanya)
"""

def cariMahasiswa(list_mahasiswa, mahasiswa):
    for i in range(len(list_mahasiswa)):
        if list_mahasiswa[i] == mahasiswa:
            return i
    return -1
    
list_mahasiswa = ["Rafi", "Andika", "Shandy", "Achmad", "Nashirul", "Mahesa", "Alwan", "Banu", "Ghaisan", "Christian", "Fadhel", "Zamzami", "Fatra", "Ariel", "Asep", "Padli", "Haryo", "Shaehyan", "Zikri", "Satrio"]
mahasiswa = input("Masukan nama Mahasiswa: ")
result = cariMahasiswa(list_mahasiswa, mahasiswa)

if (result != -1):
    print(f"{mahasiswa} ditemukan pada index ke-{result}")
else:
    print(f"{mahasiswa} tidak ditemukan di Prodi RPL!")