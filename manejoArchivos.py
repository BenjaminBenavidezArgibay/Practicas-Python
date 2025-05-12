# Ejercicio 1
datos = open("datos.txt", "w")
datos.write("Sobrescribiendo datos")
datos.close()

# Ejercicio 2
datos = open("datos.txt", "r")
lineas = datos.readlines()
datos.close()

# Ejercicio 3
datos = open("datos.txt", "a")
datos.write("\nJose\nMarcos")
datos.close()
datos = open("datos.txt", "r")
print(datos.read())
datos.close()