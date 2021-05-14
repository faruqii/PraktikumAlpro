print("\t\t Porsi Terbanyak? ")

foods = []
while True:
    amount = input("Masukkan Jumlah Porsi ('stop' untuk berhenti) : ")
    if amount == "stop":
        break
    else:
        foods.append(int(amount))
print(f"Penjualan Terbanyak dari satu pelanggan hari ini adalah: {max(foods)}")