"""Anda bekerja di departemen inventaris di perusahaan dan memiliki file "inventaris_barang.csv" yang
berisi daftar barang dan jumlahnya. Anda ingin mengupdate stok barang dengan menambahkan atau
mengurangkan jumlahnya berdasarkan pengiriman dan penjualan. Buatlah program untuk dapat
membaca dan meng-edit file ini, serta menghitung stok akhir (Buat dummy data sebanyak 20)"""

file_path = "folder/inventaris_barang.csv"

import csv
def read(file_path):
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        for line in csv_reader:
            print(line)

def write(file_path, list_header, list_data):
    with open(file_path, "w", newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=list_header, delimiter=",")
        csv_writer.writeheader()
        csv_writer.writerows(list_data)
    
def stok_akhir(file_path):
    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        total_stok = 0
        for i in csv_reader:
            if i[2] == "stok":
                continue
            total_stok += int(i[2])
        print(f"Total stok akhir adalah {total_stok}")
        
while True:
    print()
    print("Selamat datang di program inventaris barang")
    print("1. Lihat inventaris barang")
    print("2. Edit jumlah barang")
    print("3. Stok akhir barang")
    print("4. Keluar")

    pilihan = int(input("Masukkan pilihan: "))
    print()
    if pilihan == 1:
        read(file_path)
        input("\nTekan enter untuk kembali ke menu ")
    elif pilihan == 2:
        read(file_path)
        id_barang = int(input("\nMasukkan ID barang yang ingin diubah: "))
        with open (file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            list_data = []
            for line in csv_reader:
                list_data.append(line)
            for i in list_data:
                if int(i["id"]) == id_barang:
                    jumlah_barang = int(input("Masukkan jumlah barang yang ingin diubah: "))
                    if jumlah_barang > 0:
                        i["stok"] = jumlah_barang
                    else:
                        print("\nJumlah barang tidak boleh kurang dari 0")
                    break
            write(file_path, list(list_data[0].keys()), list_data)
    elif pilihan == 3:
        stok_akhir(file_path)
        input("Tekan enter untuk kembali ke menu ")
    elif pilihan == 4:
        break