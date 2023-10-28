# Studi Kasus 2
"""Berikut ini contoh dari barisan bilangan kelipatan 3: 3, 6, 9, 12, 15, 18, 21, dst.
Saat ini, Asep ingin mencari jumlah dari barisan bilangan kelipatan 3
dibawah 10. Namun, Asep ingat bahwa kemarin dia juga ingin mencari
dibawah 23. Bantulah Asep dalam mencari jumlah barisan bilangan
kelipatan 3!"""

# Jawaban
angka = int(input("Masukan angka : "))
jumlah_angka = 0
for i in range (0, angka, 3):
    jumlah_angka = jumlah_angka + i
print(f"Jumlah bilangan kelipatan 3 dibawah {angka} adalah {jumlah_angka}")