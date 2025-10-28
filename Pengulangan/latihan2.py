import random

n = int(input("Masukkan jumlah n: "))

count = 0
while count < n:
    angka = random.random()
    if angka < 0.5:
        print(angka)
        count += 1
