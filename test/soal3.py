print("\t\t === TELYU GAMING === ")
games = []
prices = []

while True:
    print("""
    1. Daftar games
    2. Cek Harga

    0. Exit
    """)

    choices = int(input("Masukkan pilihan kamu: "))
    if choices == 1:
        games.append(input("Masukkan Nama Game: "))
        prices.append(input("Masukkan Harga Game: Rp."))
    elif choices == 2:
        checks = input("Masukkan nama game: ")
        for i in range(len(games)):
            if checks == games[i]:
                print("Harga Game adalah Rp.",prices[i])
            elif checks != games[i]:
                print("Harga Game tidak ditemukan")
    elif choices == 0:
        break
    else:
        print("Error")
