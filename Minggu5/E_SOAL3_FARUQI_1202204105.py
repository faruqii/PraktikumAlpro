print("\t\t\t NOTES TEMAN BARU ")

friends = []

while True:
    name = input("Masukkan Nama teman Baru: ")
    if name == "selesai":
        break
    else:
        friends.append(name)
print("\t\t\t Teman-Teman Baru ")
print(friends)