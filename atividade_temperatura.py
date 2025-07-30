def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f + 459.67) * 5/9

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k * 9/5) - 459.67

valor = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").strip().upper()
destino = input("Unidade de destino (C, F ou K): ").strip().upper()

if origem == destino:
    resultado = valor
elif origem == "C" and destino == "F":
    resultado = celsius_para_fahrenheit(valor)
elif origem == "C" and destino == "K":
    resultado = celsius_para_kelvin(valor)
elif origem == "F" and destino == "C":
    resultado = fahrenheit_para_celsius(valor)
elif origem == "F" and destino == "K":
    resultado = fahrenheit_para_kelvin(valor)
elif origem == "K" and destino == "C":
    resultado = kelvin_para_celsius(valor)
elif origem == "K" and destino == "F":
    resultado = kelvin_para_fahrenheit(valor)
else:
    print("Unidade inválida. Use C, F ou K.")
    exit()

print(f"\nResultado: {valor}°{origem} = {resultado:.2f}°{destino}")
