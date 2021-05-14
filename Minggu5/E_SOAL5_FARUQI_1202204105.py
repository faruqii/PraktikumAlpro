database = []
voting = []
while True:
    print("""
    ===Daspro Voting===
    1.Voting
    2.Database

    0. Exit
    """)  
 
    choices = int (input("Masukkan Pilishan Anda: "))
    if choices == 1:
        name = input("Masukkan Nama Anda : ")
        database.append(name)
        print("""
        === KANDIDAT ASPRAK TERSEBUT ===
        1. XAX
        2. ADV
        3. NOP
        4. HAS
        5. IAN
        """)
        candidates = int(input("Masukkan pilishan anda (1/2/3/4)? "))
        if candidates == 1:
            voting.append("XAX")
        elif candidates == 2:
            voting.append("ADV")
        elif candidates == 3:
            voting.append("NOP")
        elif candidates == 4:
            voting.append("HAS")
        elif candidates == 5:
            voting.append("IAN")
        print(f"{name} Thank you for voting")
    elif choices == 2:
        tokens = input("Masukkan Token: ")
        if tokens == "d4spr0":
            for i in range(len(database)):
                print(database[i] + " memilih " + voting[i])
        else:
            print("Sorry Wrong Token dude!")
    elif choices == 0:
        print("Selamat Berhasil Keluar")
        break

