# Ejercicio 1
import sqlite3
def conexion():
    conn = sqlite3.connect('mi_tienda.db')
    return conn
def crearTabla():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)''')
    conn.commit()
    conn.close()
def insertar(datos):
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO productos (nombre, precio) VALUES (?, ?)''', datos)
    conn.commit()
    conn.close()
def mostrarDatos():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM productos''')
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)
    conn.close()

crearTabla()
insertar(('Producto 1', 10.0))
insertar(('Producto 2', 20.0))
insertar(('Producto 3', 30.0))
mostrarDatos()

# Ejercicio 2
def conexion():
    conn = sqlite3.connect('escuela.db')
    return conn
def crearTabla():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS estudiantes (id INTEGER PRIMARY KEY, nombre TEXT, grado INTEGER)''')
    conn.commit()
    conn.close()
def insertar(datos):
    conn = conexion()
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO estudiantes (nombre, grado) VALUES (?, ?)''', datos)
    conn.commit()
    conn.close()
def mostrarDatos():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM estudiantes''')
    estudiantes = cursor.fetchall()
    for estudiante in estudiantes:
        print(estudiante[1] + " " + str(estudiante[2]))
    conn.close()
crearTabla()
insertar([('Juan', 10), ('Maria', 11), ('Pedro', 12)])
mostrarDatos()

# Ejercicio 3
def conexion():
    conn = sqlite3.connect('bibloteca.db')
    return conn
def crearTabla():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY, titulo TEXT, año INTEGER)''')
    conn.commit()
    conn.close()
def insertar(datos):
    conn = conexion()
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO libros (titulo, año) VALUES (?, ?)''', datos)
    conn.commit()
    conn.close()
def librosActuales():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM libros WHERE año > 2000''')
    libros = cursor.fetchall()
    for libro in libros:
        print(libro[1] + " " + str(libro[2]))
    conn.close()
crearTabla()
insertar([('El Aleph', 1945), ('El tunel', 1948), ('Banco a la sombra', 2007), ('El pasado', 2003)])
librosActuales()

# Ejercicio 4
def conexion():
    conn = sqlite3.connect('empleados.db')
    return conn
def crearTabla():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (id INTEGER PRIMARY KEY, nombre TEXT, salario REAL)''')
    conn.commit()
    conn.close()
def insertar(datos):
    conn = conexion()
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO empleados (nombre, salario) VALUES (?, ?)''', datos)
    conn.commit()
    conn.close()
def empleadosOrdenados():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM empleados ORDER BY salario DESC''')
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado[1] + " " + str(empleado[2]))
    conn.close()
crearTabla()
insertar([('Juan Perez', 1500), ('Maria Gomez', 2000), ('Pedro Rodriguez', 1800), ('Ana Gomez', 1900), ('Luis Gomez', 1700)])
empleadosOrdenados()