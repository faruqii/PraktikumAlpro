name = []
while True:
    print('''
    1.Mendaftarkan Peserta
    2.Menghapus Peserta 
    3.Mencetak Semua Peserta

    0.Exit 
    ''')

    pil = int(input("Masukkan Pilihan: "))
    if pil == 1:
        name.append(input("Masukkan nama peserta: "))
    elif pil == 2:
        name.remove(input("Masukkan nama peserta: "))
    elif pil == 3:
        print(name)
    elif pil == 0:
        print("Thank You")
        break
    else:
        print("Wrong Input Sorry dude")
        
