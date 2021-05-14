age = int(input("Masukkan Umur = "))

if age >= 0 and age <= 5:
    print("Balita")
elif age >= 6 and age <= 13:
    print("Anak-anak")
elif age >=13 and age <= 17:
    print("Remaja")
elif age >= 18 and age <= 59:
    print("Dewasa")
elif age >= 60:
    print("Lansia")
else:
    print("Inputan Salah")