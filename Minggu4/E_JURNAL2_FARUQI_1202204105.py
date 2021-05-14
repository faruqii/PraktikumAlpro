class Kubus:

    def kubus(self,sisi1):
        self.sisi1 = sisi1
        Volume_kubus = sisi1 * sisi1 * sisi1 
        Luas_kubus = 6 * sisi1 * sisi1
        keliling_kubus = 12 * sisi1
        print("================================")
        print("Kubus 1")
        print(f"Volume {Volume_kubus} cm^3 ")
        print(f"Luas Permukaan {Luas_kubus} cm^2")
        print(f"Keliling {keliling_kubus} cm")

sisi1 = int(input("Masukkan sisi Kubus 1 : "))
sisi2 = int(input("Masukkan sisi Kubus 2 : "))
    
K1 = Kubus()
K1.kubus(sisi1)
K2 = Kubus()
K2.kubus(sisi2)
    