"""Andika ingin mencari jumlah bilangan yang bukan bilangan prima. Bantulah Andika untuk
menentukan jumlah bilangan yang bukan bilangan prima pada setiap bilangan yang
dimasukkan ke dalam list oleh Andika!"""

bilangan = int(input("Banyak bilangan: "))
jml_bilangan = 0

for i in range(0, bilangan):
    bilangan = int(input(f"Masukan bilangan ke-{i+1}: "))
    
    prima = True
    for i in range(2, bilangan):
        if bilangan % i == 0:
            prima = False
            break
    if prima == False:
        jml_bilangan += bilangan

print(f"Hasil penjumlahan bilangan yang bukan prima: {jml_bilangan}")