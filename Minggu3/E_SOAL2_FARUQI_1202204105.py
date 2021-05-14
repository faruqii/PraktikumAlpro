print("== COUNTDOWN SIMPLE ==")

counts = int(input())
while (counts >= 0):
    print(counts)
    counts -= 1
    if counts == 1:
        print("It's enough")
        break