"""Buatlah Program untuk menghitung volume tabung yang dibuat dalam sebuah fungsi"""
def volTabung():
    phi = 3.16
    r = jari
    t = tinggi

    vtabung = phi*r**2*t
    return(vtabung)

jari = int(input(f"Masukan jari-jari: "))
tinggi = int(input(f"Masukan tinggi: "))

print(volTabung())