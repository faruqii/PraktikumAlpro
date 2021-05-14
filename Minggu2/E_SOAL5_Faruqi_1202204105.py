berat = float(input("Masukan berat badan dalam kg: "))
tinggi = float(input("Masukan tinggi badan dalam m: "))

bmi = berat/(tinggi**2)

if bmi < 18.5:
    print(f"{bmi} termasuk kategori Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print(f"{bmi} termasuk kategori Normal")
elif bmi >= 25 and bmi < 29.9:
    print(f"{bmi} termasuk kategori Overweight")
elif bmi >= 30 and bmi < 34.9:
    print(f"{bmi} termasuk kategori Obese")
elif bmi >= 35 and bmi < 39.9:
    print(f"{bmi} termasuk kategori Very Obese")
else:
    print(f"{bmi} termasuk kategori Extremly Obese")