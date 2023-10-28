# Studi Kasus 1
"""Suhu di kota bandung saat ini 30°C. Haryo ingin mengetahui suhu tersebut
dan suhu di esok hari dalam derajat Fahrenheit (9/5 * C + 32). Bantulah
haryo untuk menghitung suhu dalam dejarat Fahrenheit menggunakan
python!"""

# Jawaban
celcius = int(input("Masukan suhu dalam celcius : "))
fahrenheit = 9/5 * celcius + 32
print(f"Suhu {celcius} derajat celcius = {fahrenheit} derajat fahrenheit")