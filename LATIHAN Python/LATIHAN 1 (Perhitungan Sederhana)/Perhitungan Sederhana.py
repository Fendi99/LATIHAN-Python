#latihan konversi satuan temperature

#latihan konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukkan Suhu Dalam Celcius: '))
print("suhu adalah", celcius, "C")

#Reamur
reamur = (4/5)*celcius
print("suhu dalam reamur adalah \t :", reamur, "R")

#Farenheit
farenheit = ((9/5)*celcius) + 32
print("suhu dalam farenheit adalah \t :", farenheit, "F")

#Kelvin
kelvin = 273 + celcius
print("suhu dalam kelvin adalah \t :", kelvin, "K")

