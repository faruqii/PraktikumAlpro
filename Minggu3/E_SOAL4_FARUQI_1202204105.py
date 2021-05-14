items = int(input("Masukkan banyak barang belanjaan: "))

prices = 0
totals = 0
x = 0
while x < items:
    prices = int(input("Masukkan harga barang: "))
    totals += prices
    x += 1
if totals > 75000:
    discount = totals * 0.80
    print(f"Total belanjaan sebelum diskon Rp.{totals}\n Total belanjaan setelah diskon Rp.{discount}")
else:
    print(f"Total belanjaan yang harus dibayar Rp.{totals}")

