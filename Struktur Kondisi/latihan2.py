a = int(input("Masukan Jumlah data (minimal 3) :"))

if a < 3:
    print("Jumlah data harus lebih dari 3!")

else:
    data = []

    for i in range(a):
        angka = int(input(f"Masukan Data ke-{i+1}:"))
        data.append(angka)

    data.sort()

    print("\aData setelah diurutkan:")
    for b in data:
        print(b)