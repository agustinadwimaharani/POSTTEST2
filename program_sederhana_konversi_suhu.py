print("konversi suhu: \n 1. Fahrenheit ke Celsius \n 2. Kelvin ke Celsius \n 3. Reamur ke Celsius")


print("\n===konversi Farenheit===")
Farenheit = float(input("masukkan nilai Farenheit: "))
Celcius = ((Farenheit - 32) * (5/9))

#konversi Farenheit

print("nilai Farenheit: ", Farenheit,"F")
print("nilai Celcius: ", Celcius, "C")


print("\n===konversi Kelvin===")
Kelvin = float(input("masukan nilai Kelvin: "))
Celcius = Kelvin - 273.15

#konversi Kelvin

print("nilai Kelvin: ", Kelvin, "K")
print("nilai Celcius: ", Celcius, "C")


print("\n===konversi Reamur===")
Reamur = float(input("masukan nilai Reamur: "))
Celcius = (5/4) * Reamur

#konversi Reamur

print("nilai Reamur: ", Reamur, "K")
print("nilai Celcius: ", Celcius, "C")


print("\n Terima Kasih!")