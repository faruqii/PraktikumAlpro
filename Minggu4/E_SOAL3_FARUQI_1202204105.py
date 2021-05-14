class Person:

    def Penyayang(self):
        print("I love you")
    def Penyabar(self):
        print("Saya Tidak Marah kok")
    def Pemaaf(self):
        print("Saya maafkan kamu")
    def SusahMoveOn(self):
        print("Kembalilah padaku")

class LakiLaki(Person):
    def Pemberani(self):
        print("Saya Tidak takut")
    def Dermawan(self):
        print("Ini saya ada rezeki buat kamu")

class Perempuan(Person):
    def Pemalu(self):
        print("Haduh Saya jadi Malu")
    def Setia(self):
        print("Akumah Cukup kamu aja")

l1 = LakiLaki()
l1.Penyayang()
l1.Penyabar()
l1.Pemaaf()
l1.SusahMoveOn()
l1.Pemberani()
l1.Dermawan()
print()
p1 = Perempuan()
p1.Penyayang()
p1.Penyabar()
p1.Pemaaf()
p1.Pemalu()
p1.Setia()
