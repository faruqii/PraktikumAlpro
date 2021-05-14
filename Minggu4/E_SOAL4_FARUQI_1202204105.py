bahan = input("Masukkan Bahan: ")

def Celana(bahan):
    if bahan == "Abaka":
        return "Keluarlah Celana Tahan Air"
    elif bahan == "Pandan":
        return "Keluarlah Celana yang Harum"
    elif bahan == "Batu":
        return "Keluarlah Celana dengan efek perlindungan maksimal"
    else:
        return f'Bahan {bahan} tidak diketahui'

print(Celana(bahan))