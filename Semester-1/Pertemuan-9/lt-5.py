"""Aira diminta guru Olahraganya untuk menghitung waktu teman-temannya mulai berlari dan selesai berlari. Ia
juga diminta untuk menghitung selisih waktu yang dia buat dan menuliskan hasilnya ke dalam format Jam -
Menit - Detik. Bantulah Aira untuk menyelesaikan masalah tersebut agar dapat dilakukan dengan cepat.
Hitung selisih jam - menit - detik."""

angka = 0
def waktu(angka):
    if angka < 0:
        return -angka
    return angka

def selisih(m, s):
    return waktu(m-s)

print("Waktu Mulai: ")
m_jam = int(input("Jam Mulai: "))
m_menit = int(input("Menit Mulai: "))
m_detik = int(input("Detik Mulai: "))

print("\nWaktu Selesai: ")
s_jam = int(input("Jam Selesai: "))
s_menit = int(input("Menit Selesai: "))
s_detik = int(input("Detik Selesai: "))

print(f"\nSelisihnya adalah {selisih(m_jam, s_jam)} jam, {selisih(m_menit, s_menit)} menit, dan {selisih(m_detik, s_detik)} detik!")
