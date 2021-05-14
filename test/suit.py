# user1 = input("Alfian, Masukkan jagoan anda : ")
# user2 = input("Nopal, Masukkan jagoan anda : ")

# # telunjuk < jempol
# # kelinking < telunjuk
# # jempol < kelingking

# if user1 == user2:
#     print("Pertandingan Seri")
# elif user1 == "jempol":
#     if user2 == "telunjuk":
#         print("ALFIAN MENANG")
#     else:
#         print("NOPAL MENANG")
# elif user1 == "telunjuk":
#     if user2 == "kelingking":
#         print("ALFIAN MENANG")
#     else:
#         print("NOPAL MENANG")
# elif user1 == "kelingking":
#     if user2 == "jempol":
#         print("ALFIAN MENANG")
#     else:
#         print("NOPAL MENANG")
# else:
#     print("ERROR")

#PT Just Code It
print("        Just Code It        ")
nama = []
while True:
    print("""
    1. Mendaftarkan Peserta
    2. Menghapus Peserta
    3. Mencetak Peserta
          
    0. Exit
     """) 

    ch = int(input("masukan pilihan : "))
    if ch == 1:
        nama.append(input("masukan nama : "))
    elif ch == 2:
        nama.remove(input("masukan nama : "))
    elif ch == 3:
        print(nama)
    elif ch == 5:
        break