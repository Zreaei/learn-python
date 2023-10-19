bilangan = int(input("masukan bilangan ganjil lebih dari 50 : "))
while (True):
    if (bilangan % 2 != 0 and bilangan > 50):
        print("benar")
        break
    else:
        bilangan = int(input("salah, inputkan lagi : "))