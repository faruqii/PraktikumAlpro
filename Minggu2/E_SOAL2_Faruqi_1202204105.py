print("===PROGRAM MIX COLOR RGB===")

color1 = input("Masukkan warna pertama: ")
color2 = input("Masukkan warna kedua  : ")

if color1 == "merah" and color2 == "biru":
    print(f"Campuran {color1} dan {color2} menghasilkan warna ungu")
elif color1 == "hijau" and color2 == "biru":
    print(f"Campuran {color1} dan {color2} menghasilkan warna cyan")
elif color1 == "merah" and color2 == "hijau":
    print(f"Campuran {color1} dan {color2} menghasilkan warna kuning")
else:
    print("PROGRAM MIX COLOR ERROR.\nMix hanya bisa untuk warna merah/hijau/biru")
