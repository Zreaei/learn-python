"""Anda adalah seorang guru yang ingin menghitung nilai rata-rata dari ujian terakhir di kelas Anda.
Anda memiliki file teks bernama "nilai_siswa.txt" yang berisi nama-nama siswa dan nilai ujian mereka.
Setiap baris dalam file ini memiliki format: "Nama Mahasiswa: Nilai". Buatlah program Anda dapat
membaca file ini dan menghitung nilai rata-rata dari ujian tersebut. (Buat dummy data sebanyak 20)"""

file_path = "Pertemuan-14/folder/nilai_siswa.txt"

def rata_rata(file_path):
    with open(file_path, "r") as file:
        total = 0
        mhs = file.readlines()
        for i in mhs:
            total += int(i.split(": ")[1])
        rata_rata = total / len(mhs)
        print(f"Rata-rata nilai ujian terakhir adalah: {rata_rata}")

rata_rata(file_path)