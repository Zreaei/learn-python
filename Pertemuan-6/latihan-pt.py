# Nomor 1
nilai = int((input("Masukan Nilai : ")))
if (nilai >= 90):
    print("Nilai anda adalah A")
elif (90 > nilai >= 80):
    print("Nilai anda adalah B")
elif (80 > nilai >= 70):
    print("Nilai anda adalah C")
elif (nilai < 70):
    print("Nilai anda adalah D")

print("")

# No 2
input_angka = input("Masukan Angka : ")
if (input_angka.isdigit()):
    input_angka = int(input_angka)
    if (input_angka % 2 == 0):
        print(f"Angka {input_angka} merupakan angka genap")
    elif (input_angka % 2 == 1):
        print(f"Angka {input_angka} merupakan angka ganjil")
else:
    print("Maaf, silahkan masukan angka")

print("")

# No 3
nilai_ujian = int(input("Masukan Nilai Ujian : "))
kondisi_keuangan = int(input("Masukan Kondisi Keuangan : "))
if (nilai_ujian >= 90 and kondisi_keuangan < 2000000):
    print("Anda berhak mendapatkan beasiswa penuh")
elif ((nilai_ujian > 80 and nilai_ujian <= 90) and kondisi_keuangan < 4000000):
    print("Anda berhak mendapatkan beasiswa parsial")
else:
    print("Anda tidak berhak mendapatkan beasiswa")

print("")

# No 4
performa = input("Masukan Performa Anda : ")
gaji = int(input("Masukan Gaji Anda : "))
if (performa == "sangat baik"):
    bonus = gaji * 20/100
    total_gaji = gaji + bonus
    print(f"Total gaji anda adalah Rp. {total_gaji} dengan bonus sebesar Rp. {bonus}")
elif (performa == "cukup"):
    bonus = gaji * 10/100
    total_gaji = gaji + bonus
    print(f"Total gaji anda adalah Rp. {total_gaji} dengan bonus sebesar Rp. {bonus}")
else:
    bonus = gaji * 5/100
    total_gaji = gaji + bonus
    print(f"Total gaji anda adalah Rp. {total_gaji} dengan bonus sebesar Rp. {bonus}")

print("")

# No 5
total_belanja = int(input("Masukan Total Belanja : "))
if (total_belanja > 500000):
    diskon = total_belanja * 10/100
    total_bayar = total_belanja - diskon
    print(f"Selamat, anda mendapatkan diskon!. Total harga yang harus anda bayar setelah diskon adalah Rp. {total_bayar}")
else:
    print(f"Maaf, anda tidak mendapat diskon. Total harga yang harus anda bayar adalah Rp. {total_belanja}")