while True:
    try:
        u = int(input("Masukkan Username: "))
        pw = input("Masukkan Password: ")

        count = 0
        for i in pw:
            count += 1 

        if u in range(0,5):
            u = True

        if u == True and pw == "alproPalingGG":
            print("Anda Berhasil Login!")

        elif u == True and pw != "alproPalingGG":
            print("Username atau password salah!")
        
        elif count < 8:
            raise NameError("Password minimal 8")

    except NameError:
            print("Password minimal 8 ")
