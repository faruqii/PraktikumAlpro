print("=== SELAMAT DATANG DI PROGRAM BUTIK")
print("""
1. Kaos
2. Kemeja
3. Jas
4. Selesai
""")
total_harga = 0 # harga awal barang
choice = int(input("Masukkan Barang Yang Ingin Dibeli (1/2/3/4) : "))
while choice != 4: # jika pilihan tidak 4 atau selesai maka program akan lanjut
    if choice == 1:
        harga = int(25000)
        print("Kaos Ditambahkan")
        total_harga += harga
        choice = int(input("Masukkan Barang Yang Ingin Dibeli (1/2/3/4) : "))
    elif choice == 2:
        harga = int(50000)
        print("Kemeja Ditambahkan")
        total_harga += harga
        choice = int(input("Masukkan Barang Yang Ingin Dibeli (1/2/3/4) : "))
    elif choice == 3:
        harga = int(100000)
        print("Jas Ditambahkan")
        total_harga += harga
        choice = int(input("Masukkan Barang Yang Ingin Dibeli (1/2/3/4) : "))
    else:
        break
print(total_harga)