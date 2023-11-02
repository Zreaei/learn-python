"""Kelompok Mutia sedang mengerjakan sebuah gim online. Mereka ingin membuat sistem
gacha kelas karakter berdasarkan tingkat keuntungan pemain. Jika pemain memiliki tingkat
keuntungan 76, pemain akan mendapatkan karakter normal. Berikut rincian ketentuan gacha
karakter tersebut!."""

keuntungan = int(input("Input: "))

if (keuntungan % 2 == 0):
    if keuntungan >= 2 and keuntungan <= 25:
        print("Sistem akan memberikan karakter Rare")
    elif keuntungan >= 26 and keuntungan <= 75:
        print("Sistem akan memberikan karakter Common")
    elif keuntungan >= 76 and keuntungan <= 90:
        print("Sistem akan memberikan karakter SSR")
    elif keuntungan >= 91 and keuntungan <= 100:
        print("Sistem akan memberikan karakter Mythic")
elif (keuntungan % 3 == 0):
    if keuntungan >= 2 and keuntungan <= 25:
        print("Sistem akan memberikan karakter SR")
    elif keuntungan >= 26 and keuntungan <= 75:
        print("Sistem akan memberikan karakter Normal")
    elif keuntungan >= 76 and keuntungan <= 90:
        print("Sistem akan memberikan karakter SSSR")
    elif keuntungan >= 91 and keuntungan <= 100:
        print("Sistem akan memberikan karakter Legendary")