INPUT_JEMPOL = "jempol"
INPUT_TELUNJUK = "telunjuk"
INPUT_KELINGKING = "kelingking"

# telunjuk < jempol
# kelinking < telunjuk
# jempol < kelingking
alfian = input("Alfian, Masukkan jagoan anda : ")
nopal = input("Nopal, Masukkan jagoan anda : ")


def suit(alfian, nopal):
    if alfian == INPUT_TELUNJUK and nopal == INPUT_JEMPOL:
        print("NOPAL MENANG")
        return
    elif alfian == INPUT_JEMPOL and nopal == INPUT_TELUNJUK:
        print("ALFIAN MENANG")
        return
    elif alfian == INPUT_KELINGKING and nopal == INPUT_TELUNJUK:
        print("NOPAL MENANG")
        return
    elif alfian == INPUT_TELUNJUK and nopal == INPUT_KELINGKING:
        print("ALFIAN MENANG")
        return
    elif alfian == INPUT_JEMPOL and nopal == INPUT_KELINGKING:
        print("NOPAL MENAG")
        return
    elif alfian == INPUT_KELINGKING and nopal == INPUT_JEMPOL:
        print("ALFIAN MENANG")
        return
    elif alfian == nopal:
        print("PERTANDINGAN SERI")
        return
    else:
        print("ERROR")
suit(alfian, nopal)
