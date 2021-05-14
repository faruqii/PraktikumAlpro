try:
    nama = input("Masukkan Nama Gen (tidak boleh kurang dari 5): ")
    assert any(nama for i in nama if not len(nama) < 5)
    n = int(input(f"Masukkan Jumlah Gen {nama} (tidak boleh 0): "))
    assert n != 0
except AssertionError:
    print("Isi Sesuai Dengan Ketentuan! ")
finally:
    print("Program Selesai")