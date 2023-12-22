import pandas as pd

# Buat file csv ke dalam dataframe
database = pd.read_csv("Daftar_Mahasiswa_2018.csv")

# Tampilkan hanya 10 data pertama
first_ten = database.head(10)
print("\n", first_ten)

# Sorting dataframe berdasarkan kolom "Nama"
sort_by_name = database.sort_values("Nama")
print("\n", sort_by_name)

# Tampilkan hanya kolom NIM, Nama, L/P, Status, SKS, IP dan Lama Studi(Smt) saja
filtered_view = database.filter(items=['NIM', 'Nama', 'L/P', 'Status', 'SKS', 'IPK', 'Lama Studi(Smt)'])
print("\n", filtered_view)

# Rata-rata IPK dari seluruh mahasiswa
average_ipk = database['IPK'].mean()
print(f"\nRata-rata IPK dari seluruh mahasiswa: {average_ipk}")

# Jumlah mahasiswa laki-laki dan perempuan
jml_laki = database['L/P'].value_counts()['L']
jml_perempuan = database['L/P'].value_counts()['P']

print(f"\nJumlah mahasiswa laki-laki: {jml_laki}")
print(f"\nJumlah mahasiswa perempuan: {jml_perempuan}")

# Tampilkan hanya data mahasiswa dengan status "Terdaftar" saja
terdaftar = database.query('`Status` == "Terdaftar" and `L/P` == "P"')
print("\n", terdaftar)

# Tampilkan seluruh mahasiswa dengan status bukan "Terdaftar"
tdk_terdaftar = database.query('`Status` != "Terdaftar"')
print("\n", tdk_terdaftar)