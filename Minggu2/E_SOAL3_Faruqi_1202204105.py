age = int(input("Masukkan umur anda: "))

if age >= 17 and age <20:
    print("Anda bisa mendapatkan SIM A,SIM C")
elif age >= 20 and age <23:
    print("Anda bisa mendapatkan SIM A,SIM C,SIM A UMUM")
elif age >= 23:
    print("Anda bisa mendapatkan SIM A,SIM C,SIM A UMUM,SIM B")
else:
    print("Anda belum bisa membuat SIM")
