"""Buatlah Program Python untuk menghitung fungsi nilai total dan nilai rata-ratanya berdasarkan nilai yang diinputkan
dari nilai total dimana banyaknya angka tidak dideklarasikan."""

def total_rata(input):
    hasil = 0

    for angka in input:
        hasil = hasil + int(angka)

    rata_rata = hasil / len(input)

    return {"hasil": hasil, "rata-rata": rata_rata}

def split(char_list, separate):
    h = []
    segment = ""

    for char in char_list:
        if char != separate:
            segment += char
        else:
            h.append(segment)
            segment = ""

    h.append(segment)
    return h
      
input = split(input("Masukan angka: "), ",")
h = total_rata(input)
separate = " + "

print(f"Total: {separate.join(input)} = {h['hasil']}")
print(f"Rata-rata: {h['hasil']} / {len(input)} = {h['rata-rata']}") 