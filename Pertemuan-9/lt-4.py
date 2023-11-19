"""Pak Dedi merupakan seorang Kepala Laboratorium Komputer di SMAN 2 Harapan. Dia
ingin membuat sebuah menu login yang dapat memberi kesempatan user untuk
memasukkan password kembali ketika dia salah sebanyak 3 kali. Ketika user terus
memasukkan password yang salah, maka user tersebut akan keluar dari menu login
tersebut. Pak budi juga menambahkan bahwa password ini harus sudah ada dalam
sistem yang di buat, sehingga sistem itu hanya mengecek password saja tanpa
memperdulikan username."""

limit = 3
def login(limit):
    username = input(f"Username: ")
    password = input(f"Password: ")

    if limit == 0:
        print(f"Anda tidak dapat login")

    if password != "Latihan":
        print(f"Password yang anda masukan salah, tersisa {limit-1} kesempatan!")
        return login(limit-1)
    elif password == "Latihan":
        print(f"Selamat datang {username}")

login(limit)
