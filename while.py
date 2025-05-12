# Ejercicio 1
contador = 1
while contador <= 5:
    print(contador)
    contador += 1


# Ejercicio 2
numero = int(input("Ingrese un numero: "))

while numero != 0:
    print(numero)
    numero = int(input("Ingrese otro numero: "))


# Ejercicio 3
while True:
    numero = int(input("Ingrese un numero: "))
    if numero < 0:
        continue
    else:
        print(f"Ingresó el numero {numero}")
        break