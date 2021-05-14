n = int(input("Masukkan Jumlah angka: "))
number = set()

for i in range(n):
    y = int(input(f'Masukkan angka ke-{i+1}: '))
    number.add(y)
print(list(number))

