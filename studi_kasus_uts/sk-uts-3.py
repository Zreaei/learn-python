"""Bagas ingin menjabarkan angka-angka dari faktorial 8. Faktorial dianotasikan menggunakan
tanda seru (n! = n * (n – 1)!). Bantulah Bagas dalam membuat program Python berdasarkan
Test Case berikut!
"""

angka = int(input("Faktorial: "))

for i in range(0, angka):
    if i + 1 != angka:
        print(f"{angka - i}! = {angka - i} * {angka - i - 1}!")  
    else:
        print(f"{angka - i}! = {angka - i}")