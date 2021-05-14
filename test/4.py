try:
    print("Program Penentu Index")
    nilai_akhir = float(input("Masukkan Nilai Akhir Anda! : "))
    if not type(nilai_akhir) is float:
        raise ValueError
    elif nilai_akhir > 100 or nilai_akhir < 0:
        raise NameError
except ValueError:
    print("Input harus berupa angka! (int/float)")
except NameError:
    print("Nilai minimal 0 dan maksimal 100")
else:
    if nilai_akhir >= 80:
        print("Indeks kamu adalah : A")
    elif 40 < nilai_akhir < 80:
        print("Indeks kamu adalah : B")
    elif nilai_akhir <= 40:
        print("Indeks kamu adalah : C")
finally:
    print("Program selesai")
