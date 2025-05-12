# Ejercicio 1
dic = {'hola': 'hello', 'azul': 'blue'}
print(dic)
dic['azul'] = 'rojo'
print(dic)

# Ejercicio 2
colores = {'rojo': 'red', 'verde': 'green', 'azul': 'blue'}
print(colores)
del(colores['azul'])
print(colores)

# Ejercicio 3
auto = {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2020, 'precio': {'pesos': 100000, 'dolares': 1000}}
print(auto['precio']['dolares'])
auto['precio']['pesos'] = 200000
print(auto)

# Ejercicio 4
lista_de_dicc = []
lista_de_dicc.append(auto)
print(lista_de_dicc[0]['modelo'])
