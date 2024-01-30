# if
nilai = 90
if (nilai >= 70):
    print("Anda Lulus")

# if else
nilai = 69
absen = "Hadir"
if (nilai >= 70) and (absen == "Hadir"):
    print("Anda Lulus")
else:
    print("Anda tidak lulus")

# else if
nilai = 69
absen = "Hadir"
sikap = "Baik"
if (nilai >= 70) and (absen == "Hadir"):
    print("Anda Lulus")
elif (absen == "Hadir") and (sikap == "Baik"):
    print("Anda lulus karena berkelakuan baik")
else:
    print("Anda tidak lulus")