day = int(input("Masukkan nomor Hari : "))

# if day == 1:
#     print(f"hari ke- {day} adalah Hari Senin")
# elif day == 2:
#     print(f"hari ke- {day} adalah Hari Selasa")
# elif day == 3:
#     print(f"hari ke- {day} adalah Hari Rabu")
# elif day == 4:
#     print(f"hari ke- {day} adalah Hari Kamis")
# elif day == 5:
#     print(f"hari ke- {day} adalah Hari Jumat")
# elif day == 6:
#     print(f"hari ke- {day} adalah Hari Sabtu")
# elif day == 7:
#     print(f"hari ke- {day} adalah Hari Minggu")
# else:
#     print(f"Tidak Ada hari ke- {day}")
    

match day:
    case 1:
        print(f"hari ke- {day} adalah Hari Senin")
    case 2:
        print(f"hari ke- {day} adalah Hari Selasa")
    case 3:
        print(f"hari ke- {day} adalah Hari Rabu")
    case 4:
        print(f"hari ke- {day} adalah Hari Kamis")
    case 5:
        print(f"hari ke- {day} adalah Hari Jumat")
    case 6:
        print(f"hari ke- {day} adalah Hari Sabtu")
    case 7:
        print(f"hari ke- {day} adalah Hari Minggu")
    case _:
        print(f"Tidak Ada hari ke- {day}")
