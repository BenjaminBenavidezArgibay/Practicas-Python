# Ejercicio 1
numero = int(input("Ingrese un numero: "))

if numero > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo o igual a cero")


# Ejercicio 2
calificacion = int(input("Ingrese una calificacion: "))

if calificacion >= 90:
    print("A")
elif calificacion <90 and calificacion >= 80:
    print("B")
elif calificacion <80 and calificacion >= 70:
    print("C")
else:
    print("F")


# Ejercicio 3
edad = int(input("Ingrese su edad: "))

if edad < 18 or edad > 65:
    print("No estás en el rango permitido para trabajar")
else:
    print("Estás en el rango permitido para trabajar")


# Ejercicio 4
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if numero1 > 0 and numero2 > 0:
    print("Ambos numeros son positivos")
else:
    print("No ambos numeros son positivos")
