print("====Operasi Pembagian====")
try:
    num1 = int(input("Masukkan angka pertama\t: "))
    num2 = int(input("Masukkan angka kedua\t: "))
    bagi = num1/num2
except ZeroDivisionError:
    print("Anda tidak dapat membagi bilangan dengan 0")
else:
    print(f"Hasil pembagian\t\t: {bagi}")

