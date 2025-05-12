# # Ejercicio 1
try:
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    resultado = numero1 / numero2
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")


# # Ejercicio 2
try:
    numero = int(input("Ingrese un numero: "))
    print(numero)
except ValueError:
    print("Error: El valor ingresado no es un numero")


# Ejercicio 3
try:
    texto = input("Ingrese un texto: ")
    if not texto:
        raise ValueError("El texto no puede estar vacío")
    print(texto)
except ValueError as e:
    print(f"Error: {e}")

