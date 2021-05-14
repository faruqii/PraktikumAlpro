print("=== Program Konversi Suhu ===")

suhu = int(input("Masukkan Suhu Reamur  : "))

celcius = float(5/4 * suhu) #rumus reamur ke celcius
farenheit = float(9/4 * suhu + 32) #rumus reamur ke farenheit
kelvin = float(5/4 * suhu + 273) # rumus reamur ke kelvin

print(suhu," Reamur ke Celcius   = ",celcius)
print(suhu," Reamur ke Farenheit = ",farenheit)
print(suhu," Reamur ke  kelvin   = ",kelvin)