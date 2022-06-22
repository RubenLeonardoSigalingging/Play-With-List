#!/usr/bin/env python3


# Created by: Ruben Leonardo Sigalingging.
# Created on: Wednesday, June 22, 2022, 9:04 PM.
# ---PLAY WITH LISTS IN PYTHON 3.8.10 PROGRAMMING---


# Dibuat oleh: Ruben Leonardo Sigalingging.
# Dibuat pada: Rabu, 22 Juni 2022, Pukul 9:04 Malam.
# ---BERMAIN DENGAN DAFTAR DI PEMROGRAMAN PYTHON 3.8.10---


# Using Indonesia Language.


from os import system
system("clear")


# list untuk menampung nama-nama buah
buah_buahan=["Pir","Pepaya","Semangka","Pisang","Jambu","Mangga","Alpukat","Salak","Rambutan","Durian","Nanas","Chocolate"]
# Tampilkan isi list "buah_buahan" dengan nomor index 3
print("Isi Buah-buahan Index Ke 3: {}".format(buah_buahan[3]))
# Tampilkan semua daftar buah-buahan
print("Semua Buah-buahan Berjumlah {}".format(len(buah_buahan)))
for buah_itu_sehat in buah_buahan:
	print(buah_itu_sehat)


# ---MENGGANTI NILAI LIST---
# list mula-mula
bahasa=["Indonesia","Inggris","Mandarin","Spanyol","Italia"]
# mengubah nilai index ke 2
bahasa[2]="Belanda"
print(bahasa)


# ---MENAMBAHKAN ITEM LIST---
# list awal
buah=["Jeruk","Apel","Sirsak","Leci"]
# tambahkan buah duren
buah.append("Anggur")
print(buah)


# ---MENGHAPUS ITEM LIST---
belajar=[
"Belajar Python",
"Belajar Ruby",
"Belajar Perl",
"Belajar Sulap",
"Belajar C++"
]
# hapus "Belajar Sulap"
del belajar[3]
print(belajar)
# contoh 2
sifat=[
"Baik",
"Jahat",
"Sombong",
"Ramah",
"Periang",
"Sabar",
"Angkuh",
"Dermawan"
]
sifat.remove("Jahat")
print(sifat)
sifat.pop()
print(sifat)


# ---MEMBALIK LIST---
x=[1,2,3,4,5]
x.reverse()
print(x)


# ---MENGURUTKAN LIST---
x=[9,8,3,1,2,5]
x.sort()
print(x)


a=[8,9,5,3,6,1,2]
b=a[:] 
# MENGCOPY SEMUA ISI LIST A KE LIST B
a.sort()
# MENGURUTKAN ISI LIST b
print(a)
print(b)