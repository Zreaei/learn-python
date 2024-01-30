# Studi Kasus 5
"""Fatra mempunyai banyak teman yang namanya sangat umum, seperti
Asep, Asep, Asep, Anisa, Anisa, Dimas, Dewi, Dewi, Putri, Putri, Putri, dan Putra.
Fatra bisa saja menghitung secara manual jumlah temannya yang
bernama sama tersebut. Namun, Fatra ingin membuat program python
yang dapat menghitung jumlah tersebut dan dikelompokkan
menggunakan Dictionary python. Bantulah Fatra dalam membuat program
tersebut!
"""

# Jawab
list_nama = input("Nama teman: ").lower().replace(" ", "").split(",")
dict_teman = {}

for nama in list_nama:
    if nama in dict_teman:
        dict_teman[nama] += 1
    else:
        dict_teman[nama] = 1

print(dict_teman)