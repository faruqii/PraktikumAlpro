nama = str(input("Nama  : "))
kelas = str(input("Kelas : "))
nim = str(input("NIM   : "))

nilai1 = float(input("Masukkan nilai kuis 1: "))
nilai2 = float(input("Masukkan nilai kuis 2: "))
nilai3 = float(input("Masukkan nilai kuis 3: "))

rata = float( (nilai1 + nilai2 + nilai3) / 3 ) # rumus rata-rata
print("Rata-Rata Kuis: ",rata)