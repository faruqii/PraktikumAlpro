nama = []
Pilihan = []

while True:
    print("""=== DASPRO VOTING ===\n
    1. Voting
    2. Database

    0. Exit 
    """)
    pil = int(input("Masukkan Pilihan Anda: "))
    if pil == 1:
        user = input("Masukkan Nama Anda: ")
        print(""" === KANDIDAT ASPRAK TERIMUT === 
        1. XAX 
        2. ADV
        3. NOP
        4. HAS
        5. IAN
        """)
        vote = int(input("Masukkan Pilihan (1/2/3/4/5) : "))
        if vote == 1:
            Pilihan.append("XAX")
        elif vote == 2:
            Pilihan.append("ADV")
        elif vote == 3:
            Pilihan.append("NOP")
        elif vote == 4:
            Pilihan.append("HAS")
        elif vote == 5:
            Pilihan.append("IAN")
        nama.append(user)    
    if pil == 2:
        token = input("Masukkan Token: ")
        if token == "d4spr0":
            for i in range(len(nama)):
                print(nama[i],"memilih",Pilihan[i])

