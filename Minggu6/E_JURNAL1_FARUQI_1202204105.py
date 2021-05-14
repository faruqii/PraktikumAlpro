try:
    number = int(input("Masukkan Angka: "))
except ValueError:
    print("Hanya Menerima Angka!! ")
else:
    print(number)