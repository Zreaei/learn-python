"""Kelompok Risti dan Nashirul akan membuat program yang bisa membaca barisan bilangan
bulat positif. Mereka ingin program tersebut berhenti membaca ketika pengguna
memasukkan bilangan negatif dan mencetak masing-masing jumlah bilangan kelipatan 4 dan
5. Bantulah mereka dalam membuat program tersebut menggunakan Python!"""

jml_kel_4 = 0
jml_kel_5 = 0
bilangan = 0

while not bilangan < 0:
    if bilangan % 4 == 0:
        jml_kel_4 += bilangan
    if bilangan % 5 == 0:
        jml_kel_5 += bilangan

    bilangan = int(input("Input: "))
    
    if bilangan < 0:
        print(f"Jumlah bilangan kelipatan 4: {jml_kel_4}")
        print(f"Jumlah bilangan kelipatan 5: {jml_kel_5}")
        break