# Ejercicio 1
lista = [True, False, 1, 2, 3, "Hola", "Bienvenido"]
print(lista)
print(lista[-1])
lista[2] = "chau"
print(lista)

# Ejercicio 2
numeros = [10, 20, 30, 40, 50, 60]
numeros1 = numeros[2:4]
print(numeros1)
numeros2 = numeros[:5]
print(numeros2)

# Ejercicio 3
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2])

# Ejercicio 4
lista1 = [False, 2.3, "Hola", True, 234]
lista1.append("Hola")
lista1.insert(0, "Chau")
lista1.pop(1)
lista1.remove("Hola")
print(len(lista1), lista1.count("Hola"), lista1.index("Hola"))