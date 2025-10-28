# Tugas-Praktikum-6

Berikut adalah penjelasan dari setiap code

# Pengungangan

-Latihan 1
1. for i in range(5):
Perulangan luar ini akan menjalankan i dari 0 sampai 4 (karena range(5) menghasilkan: 0, 1, 2, 3, 4).
Jadi total ada 5 kali perulangan.
2. for j in range(5):
Di dalam setiap nilai i, ada perulangan dalam yang juga berjalan dari 0 sampai 4.
Jadi untuk setiap satu nilai i, j juga berulang sebanyak 5 kali.
3. print(i + j, end=' ')
Pada setiap kombinasi i dan j, program mencetak hasil penjumlahan i + j.
Parameter end=' ' membuat hasilnya dicetak di baris yang sama dengan spasi antar nilainya (bukan pindah ke baris baru).
4. print()
Setelah perulangan j selesai (satu baris selesai dicetak), baris ini membuat pindah ke baris baru, supaya hasil berikutnya dicetak di bawahnya.

-Latihan 2
1. import random
Mengimpor modul random dari Python.
Modul ini berisi fungsi-fungsi untuk menghasilkan angka acak.
2. n = int(input("Masukkan jumlah n: "))
Program meminta pengguna memasukkan sebuah bilangan bulat (n).
Nilai ini menentukan berapa banyak angka acak yang ingin ditampilkan (yang kurang dari 0.5).
Contoh:
Masukkan jumlah n: 3
Berarti program akan mencetak 3 angka acak yang nilainya < 0.5.
3. count = 0
Variabel count digunakan sebagai penghitung berapa banyak angka yang sudah dicetak sejauh ini.
4. while count < n:
Selama jumlah angka yang dicetak (count) belum mencapai n, program akan terus mengulang perintah di dalam blok while.
5. angka = random.random()
Menghasilkan angka acak antara 0.0 dan 1.0
(contohnya: 0.2345, 0.8321, dll).
6. if angka < 0.5:
Mengecek apakah angka acak yang baru dihasilkan kurang dari 0.5.
Jika ya (True) → angka akan dicetak dan count bertambah 1.
Jika tidak (False) → angka tidak dicetak, dan count tidak berubah. Loop akan lanjut mencoba lagi.
7. print(angka)
Mencetak angka yang kurang dari 0.5 ke layar.
8. count += 1
Menambah nilai penghitung count sebanyak 1 setiap kali angka dicetak.

# Struktur-Kondisi

-Latihan 1
1. Bagian input:
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

Program meminta pengguna memasukkan 4 bilangan bulat, lalu menyimpannya ke variabel:
a → bilangan pertama
b → bilangan kedua
c → bilangan ketiga
d → bilangan keempat

Contoh:
Masukkan bilangan pertama: 12
Masukkan bilangan kedua: 7
Masukkan bilangan ketiga: 25
Masukkan bilangan keempat: 19

3. Menentukan nilai awal terbesar:
terbesar = a
Di awal, program menganggap bilangan a sebagai yang terbesar sementara.
Nanti akan dibandingkan dengan bilangan lain satu per satu.

5. Membandingkan dengan bilangan kedua:
if b > terbesar:
   terbesar = b
Kalau ternyata b lebih besar dari nilai terbesar saat ini (a), maka update nilai terbesar menjadi b.

7. Membandingkan dengan bilangan ketiga:
if c > terbesar:
    terbesar = c
Jika c lebih besar dari nilai terbesar saat ini, maka nilai terbesar diganti menjadi c.

9. Membandingkan dengan bilangan keempat:
if d > terbesar:
    terbesar = d
Sama seperti sebelumnya — jika d lebih besar, maka terbesar diganti dengan d.

11. Menampilkan hasil:
print("Bilangan terbesar adalah:", terbesar)
Setelah semua perbandingan selesai, nilai terbesar pasti menyimpan bilangan paling besar dari keempat input.

-Latihan 2
1. a = int(input("Masukan Jumlah data (minimal 3) :"))
Program meminta pengguna untuk mengetik berapa banyak data (angka) yang ingin dimasukkan.
Nilai ini disimpan di variabel a.
Contoh:
Masukan Jumlah data (minimal 3) : 5

3. if a < 3:
Mengecek apakah jumlah data yang dimasukkan kurang dari 3.

4. print("Jumlah data harus lebih dari 3!")
Jika pengguna memasukkan angka kurang dari 3, program akan menampilkan pesan error dan tidak melanjutkan proses.

5. else:
Jika jumlah data 3 atau lebih, maka program melanjutkan ke proses penginputan data.

6. data = []
Membuat list kosong untuk menampung semua angka yang dimasukkan nanti.

7. Perulangan penginputan data:
for i in range(a):
    angka = int(input(f"Masukan Data ke-{i+1}:"))
    data.append(angka)

Penjelasan:
for i in range(a) artinya program akan mengulang sebanyak jumlah data (a).
input(f"Masukan Data ke-{i+1}:") menampilkan teks dinamis, misalnya:
Masukan Data ke-1:
Masukan Data ke-2:
...
data.append(angka) → menambahkan angka yang dimasukkan ke dalam list data.
Contoh hasil setelah input:
data = [12, 5, 20, 7, 15]

8. data.sort()
Mengurutkan isi list data dari kecil ke besar (ascending order).
Dari contoh sebelumnya:
sebelum: [12, 5, 20, 7, 15]
sesudah: [5, 7, 12, 15, 20]

9. print("\aData setelah diurutkan:")
Mencetak teks hasilnya.
Karakter \a adalah "bell character" yang akan membuat bunyi “beep” kecil di terminal (jika terminal mendukungnya).

10. Menampilkan hasil:
for b in data:
    print(b)
Menampilkan setiap angka di list data satu per satu dalam baris baru.
Output:
Data setelah diurutkan:
5
7
12
15
20
