

# un = "4105"
# pw = "alproPalingGG"
# for i in range(3):
#    try:
#        username = input("Masukkan Username : ")
#        password = input("Masukkan password : ")
#        if len(password) < 8:
#            raise NameError
#        else:
#            if un == username and pw == password:
#                print("Anda berhasil login!")
#                break
#            else:
#                print("Username atau password salah!")
#    except NameError:
#        print("Password minimal 8 bro!")
#        continue

vio = "4101"
pasw = "alproPalingGG"

for i in range(3):
    try:
        us = input("Masukkan Username: ")
        pw = input("Masukkan Password: ")
        if len(pw) < 8:
            raise NameError
        else:
            if us == "4101" and pw == "alproPalingGG":
                print("Berhasil Login")
                break
            else:
                print("Username atau password salah!")
    except NameError:
        print("Password Minimal 8 bro!")