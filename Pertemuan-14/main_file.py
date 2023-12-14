# Membuka file
file = open("Pertemuan-14/folder/file.txt", "r")

content = file.read()
print(content)

# Menutup file
file.close()

# Membaca file menggunakan with open
with open("Pertemuan-14/folder/file.txt", "r") as file:
    content = file.read()
    print(content)

# Membaca file dengan menentukan banyak karakter yang ditampilkan
with open("Pertemuan-14/folder/file.txt", "r") as file:
    content = file.read(20)
    print(content)

# Membaca file dengan readline
with open("Pertemuan-14/folder/file.txt", "r") as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()

# Membaca file menggunakan iterasi langsung
with open("Pertemuan-14/folder/file.txt", "r") as file:
    for line in file:
        print(line)

# Menulis pada file yang sudah ada dengan metode write()
with open("Pertemuan-14/folder/old_file.txt", "w") as file:
    file.write("Tulisan ini akan ditulis ke dalam berkas yang sudah ada")
    
# Menulis pada file yang belum ada dengan metode write()
with open("Pertemuan-14/folder/new_file.txt", "w") as file:
    file.write("Tulisan ini akan ditulis ke dalam berkas baru yang sebelumnya tidak ada")

# Membaca file yang telah ditulis menggunakan metode write()
with open("Pertemuan-14/folder/new_file.txt", "r") as file:
    content = file.read()
    print(content)

# Membaca isi dari file sebelum menambahkan text dengan mode append()
with open ("Pertemuan-14/folder/old_file.txt", "r") as file:
    content = file.read()
print(content)

# Menuliskan tulisan ke dalam file yang sudah ada
with open("pertemuan-14/folder/old_file.txt", "a") as file:
    file.write("Tulisan ini baru ditambahkan pada file yang sudah ada")

print("\n------------------*****------------------\n")

# Membaca isi dari file
with open("pertemuan-14/folder/old_file.txt", "r") as file:
    content = file.read()
print(content)

# Menuliskan tuliskan ke dalam file yang belum ada
with open("Pertemuan-14/folder/new_file_append.txt", "a") as file:
    file.write("Tulisan ini baru ditambahkan dengan mode append pada file yang belum ada")

# Membaca isi dari file
with open("Pertemuan-14/folder/new_file_append.txt", "r") as file:
    content = file.read()
print(content)

# Membaca isi dari file sebelum menambahkan text dengan metode writelines()
with open("Pertemuan-14/folder/new_file_append.txt", "r") as file:
    content = file.read()
print(content)

# Menuliskan tulisan ke dalam file yang sudah ada
with open ("Pertemuan-14/folder/old_file.txt", "w") as file:
    lines = ["Ini\n", "adalah\n", "tulisan\n", "baru\n", "dengan\n", "metode\n", "writelines()\n"]
    file.writelines(lines)

print("\n------------------*****------------------\n")

# Membaca isi dari file
with open("Pertemuan-14/folder/old_file.txt", "r") as file:
    content = file.read()
print(content)

# Memeriksa ketersediaan file menggunakan os.path.exists(true)
import os

file = os.path.exists("Pertemuan-14/folder/new_file.txt")

if file:
    print("Ok, berkas ada")
else:
    print("Maaf, berkas tidak ditemukan")

# Memeriksa ketersediaan file menggunakan os.path.exists(false)
import os

file = os.path.exists("Pertemuan-14/folder/tidak_ada.txt")

if file:
    print("Ok, berkas ada")
else:
    print("Maaf, berkas tidak ditemukan")

# Memeriksa tipe file menggunakan os.path.isfile(true)
import os

file = os.path.isfile("Pertemuan-14/folder/new_file.txt")

if file:
    print("Ini adalah file")
else:
    print("Ini bukan file atau file tidak ada")

# Memeriksa tipe file menggunakan os.path.isfile(false)
import os

file = os.path.isfile("Pertemuan-14/folder/folder.txt")

if file:
    print("Ini adalah file")
else:
    print("Ini bukan file atau file tidak ada")

# Membuat file berisi list
import os

# Membuat variabel untuk path file
file_path = "Pertemuan-14/folder/file_list.txt"

# Mengecek apakah file tersebut ada atau tidak
if os.path.exists(file_path):
    # Membuka isi file dan menyimpan setiap baris ke dalam list yang bernama lines
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Menghapus karakter newline ("\n") dari setiap baris dan kemudian membagi setiap baris berdasarkan spasi
    list_data = []
    for line in lines:
        new_line = line.strip().split()
        list_data.append(new_line)

    # Menampilkan isi file yang telah dibaca
    for item in list_data:
        print(item)

else:
    print(f"Maaf file untuk {file_path} tidak ditemukan")

# Menyimpan list ke dalam file baru
list = ['mangga', 'strawberry', 'pisang', 'anggur', 'salak', 'apel', 'jeruk', 'semangka', 'durian']

with open("Pertemuan-14/folder/list_to_file.txt", "w") as file:
    hasil = ' '.join(list)
    file.write(hasil)
