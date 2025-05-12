# Ejercicio 1
import sqlite3

def conexion():
    conn = sqlite3.connect('mi_base.db')
    print("Conexión exitosa")
    return conn

def cerrarConexion(conn):
    conn.close()
    print("Conexión cerrada")

cerrarConexion(conexion())


# Ejercicio 2
def conexion():
    conn = sqlite3.connect('escuela.db')
    return conn
def crearTabla():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, edad INTEGER)''')
    conn.commit()
    conn.close()
    
crearTabla()


# Ejercicio 3
def conectar():
    conn= sqlite3.connect('empresa.db')
    return conn
def crearTablas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE departamentos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL
    )''')
    cursor.execute('''CREATE TABLE empleados (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        cargos TEXT NOT NULL,
        departamento_id INTEGER,
        FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
    )''')
    conn.commit()
    conn.close()


# Ejercicio 4
def conexion():
    conn = sqlite3.connect('biblioteca.db')
    return conn
def crearTabla():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE libros (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, año_publicacion INTEGER, precio REAL)''')
    conn.commit()
    conn.close()