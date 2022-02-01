round = int(input("Banyak ronde? "))

tami_win = 0
boi_win = 0

for i in range(round):
    user_1 = input("Tami pilih apa? (B/G/K) ")
    user_2  = input("Boi pilih apa? (B/G/K) ")
    if user_1 == "B" and user_2 == "G":
        tami_win += 1 
    elif user_1 == "G" and user_2 == "K":
        tami_win += 1
    elif user_1 == "K" and user_2 == "B":
        tami_win += 1
    elif user_1 == user_2:
        continue
    else:
        boi_win += 1
        
if tami_win > boi_win:
    print("Selamat tami menang sebanyak",tami_win,"ronde")
elif tami_win == boi_win:
    print("SERI")
else:
    print("Selamat boi menang sebanyak",boi_win,"ronde")
