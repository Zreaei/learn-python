import pandas as pd

data_jual = pd.read_csv("data_penjualan.csv", parse_dates=['Tanggal'])

# Total pendapatan setiap bulan
januari = data_jual.loc[data_jual['Tanggal'].dt.month == 1]['Total'].sum()
februari = data_jual.loc[data_jual['Tanggal'].dt.month == 2]['Total'].sum()
maret = data_jual.loc[data_jual['Tanggal'].dt.month == 3]['Total'].sum()
april = data_jual.loc[data_jual['Tanggal'].dt.month == 4]['Total'].sum()
mei = data_jual.loc[data_jual['Tanggal'].dt.month == 5]['Total'].sum()
juni = data_jual.loc[data_jual['Tanggal'].dt.month == 6]['Total'].sum()
juli = data_jual.loc[data_jual['Tanggal'].dt.month == 7]['Total'].sum()
agustus = data_jual.loc[data_jual['Tanggal'].dt.month == 8]['Total'].sum()
september = data_jual.loc[data_jual['Tanggal'].dt.month == 9]['Total'].sum()
oktober = data_jual.loc[data_jual['Tanggal'].dt.month == 10]['Total'].sum()
november = data_jual.loc[data_jual['Tanggal'].dt.month == 11]['Total'].sum()
desember = data_jual.loc[data_jual['Tanggal'].dt.month == 12]['Total'].sum()

print(f"Total pendapatan bulan Januari: {januari}")
print(f"Total pendapatan bulan Februari: {februari}")
print(f"Total pendapatan bulan Maret: {maret}")
print(f"Total pendapatan bulan April: {april}")
print(f"Total pendapatan bulan Mei: {mei}")
print(f"Total pendapatan bulan Juni: {juni}")
print(f"Total pendapatan bulan Juli: {juli}")
print(f"Total pendapatan bulan Agustus: {agustus}")
print(f"Total pendapatan bulan September: {september}")
print(f"Total pendapatan bulan Oktober: {oktober}")
print(f"Total pendapatan bulan November: {november}")
print(f"Total pendapatan bulan Desember: {desember}")

# Rata-rata pendapatan 2023
rata_pendapatan = data_jual['Total'].mean()
print(f"Rata-rata pendapatan 2023: {rata_pendapatan}")

# Pendapatan paling sedikit dan paling banyak
max_pendapatan = data_jual['Total'].max()
min_pendapatan = data_jual['Total'].min()

print(f"Pendapatan paling sedikit: {min_pendapatan}")
print(f"Pendapatan paling banyak: {max_pendapatan}")

# Produk terlaris yang paling banyak terjual
terlaris = data_jual.loc[data_jual['Jumlah'].idxmax()]
print(f"Produk terlaris adalah: {terlaris['Produk']}")
