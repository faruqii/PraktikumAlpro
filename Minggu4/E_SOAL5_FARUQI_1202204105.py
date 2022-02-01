class User:

    def login(self):
        user = input("Username :")
        pw = input("Password :")

        if user == "alpro" and pw == "daspro":
            print('Login Success')
            print('Welcome to my app!!')
        elif user != "alpro" and pw != "daspro":
            print('Login Failure, Wrong Password')
    def logout(self):
        print("You're successfully logged out. Thank you for using me ")

if __name__ == "__main__":
    Status = False
    while True:
        print('User Testing Application')
        print('''1. Login''')
        print('''2. Logout''')

        u_input = int(input("Choose Menu? :"))

        if u_input == 1:
            app = User()
            app.login()
            Status = True
            print()
        elif u_input == 2 and Status == False:
            print("!!Login First!!")
        elif u_input == 2 and Status == True:
            app.logout()
            break
        else:
            print("!!No Option!!")
            break
