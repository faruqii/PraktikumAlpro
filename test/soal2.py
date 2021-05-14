print("<<< PROGRAM KELIPATAN ANGKA >>>")

limits = int(input("Masukkan Batas Angka: "))
multiples = int(input("Masukkan Kelipatan Angka: "))

for i in range(0,limits,multiples):
    print(i,end = " ")
    