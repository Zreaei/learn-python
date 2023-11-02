"""Achmad ingin membuat sistem sign-in pada aplikasi e-money menggunakan kode akses
yang telah terdaftar (kode akses: adm123). Namun, sistem sign-in tersebut dibatasi
sebanyak 3 kali percobaan jika pengguna salah memasukan kode pin-nya. Bantulah Achmad
dalam membuat sistem sign-in menggunakan bahasa pemrograman python!"""

kode = ""
kesempatan = 3
while True:
    kode = input("Kode: ")
    kesempatan -= 1   
    if kesempatan == 0:
        print("Anda tidak bisa mengakses aplikasi ini")
        break
    elif kode == "adm123":
        print("Selamat datang di aplikasi Achmad Pay")
        break
    else:
        print(f"Salah!, (sisa {kesempatan}x kesempatan)")

