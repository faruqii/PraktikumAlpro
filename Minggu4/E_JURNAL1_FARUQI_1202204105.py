class Student:

    def __init__(self,nama,nim,kelas,alamat):
        self.nama = nama
        self.nim = nim
        self.kelas =kelas 
        self.alamat = alamat

    def show(self):
        print("Nama\t: ",self.nama)
        print("NIM\t: ",self.nim)
        print("Kelas\t: ",self.kelas)
        print("Alamat\t: ",self.alamat)

print("Mahasiswa 1")    
m1 = Student("Ananda","1202190008","SI-43-02","Palangkaraya")
m1.show()
print()
print("Mahasiswa 2")
m2 = Student("Xaximi","12021902937","SI-42-04","Bogor")
m2.show()
print()
print("Mahasiswa 3")
m3 = Student("Rizal","1202128729","SI-43-01","Bandung")
m3.show()