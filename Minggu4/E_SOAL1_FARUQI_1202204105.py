def add(num1,num2,num3):
    return num1 + num2 + num3
def subtract(num1,num2,num3):
    return num1 - num2 - num3
def multiply(num1,num2,num3):
    return num1 * num2 * num3
def divide(num1,num2,num3):
    return num1 / num2 / num3

num1 = int(input("Masukkan Bilangan 1: "))
num2 = int(input("Masukkan Bilangan 2: "))
num3 = int(input("Masukkan Bilangan 3: "))

print("Hasil Pertambahanan ketiga bilangan adalah",add(num1,num2,num3))
print("Hasil Perkurangan ketiga bilangan adalah",subtract(num1,num2,num3))
print("Hasil Perkalian ketiga bilangan adalah",multiply(num1,num2,num3))
print("Hasil Pembagian ketiga bilangan adalah",divide(num1,num2,num3))