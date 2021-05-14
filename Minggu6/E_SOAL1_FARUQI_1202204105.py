try:
    num1 = int(input("Masukkan Bilangan ke 1: "))
    num2 = int(input("Masukkan Bilangan ke 2: "))
    bagi = (num1 / num2) or (num2 / num1)
except ValueError:
    print("Tipe Data Kamu Tidak Sesuai! ")
except ZeroDivisionError:
    print("Program Tidak Dapat Membagi operasi pembagian dengan nol")
else:
    print(f"TOTAL HASIL PEMBAGIAN ADALAH = {bagi}")