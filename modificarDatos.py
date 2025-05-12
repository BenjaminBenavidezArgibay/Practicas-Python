# Ejercicio 1
import sqlite3
def conexion():
    conn = sqlite3.connect('empresa.db')
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
def cambiarSalario():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''UPDATE empleados SET salario = salario * 1.10 WHERE ID = 2''')
    conn.commit()
    conn.close()
def empleadosActuales():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM empleados''')
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado[1] + " " + str(empleado[2]))
    conn.close()
crearTabla()
insertar([('Juan', 1000), ('Ana', 1500), ('Luis', 2000), ('Maria', 2500)])
cambiarSalario()
empleadosActuales()

# Ejercicio 2
def conexion():
    conn = sqlite3.connect('inventario.db')
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
    cursor.executemany('''INSERT INTO productos (nombre, precio) VALUES (?, ?)''', datos)
    conn.commit()
    conn.close()
def cambiarPrecio():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''UPDATE productos SET precio = precio * 1.20 WHERE precio > 5000''')
    conn.commit()
    conn.close()
def productosActuales():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM productos''')
    productos = cursor.fetchall()
    for producto in productos:
        print(producto[1] + " " + str(producto[2]))
    conn.close()
crearTabla()
insertar([('Chocolate', 1000), ('Leche', 1500), ('Arroz', 2000), ('Alfajor', 2500), ('Turron', 3000)])
cambiarPrecio()
productosActuales()

# Ejercicio 3
def conexion():
    conn = sqlite3.connect('biblioteca.db')
    return conn
def crearTabla():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT)''')
    conn.commit()
    conn.close()
def insertar(datos):
    conn = conexion()
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO libros (titulo, autor) VALUES (?, ?)''', datos)
    conn.commit()
    conn.close()
def borrarLibro():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM libros WHERE titulo = 'Libro Eliminado' ''')
    conn.commit()
    conn.close()
def librosActuales():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM libros''')
    libros = cursor.fetchall()
    for libro in libros:
        print(libro[1] + " " + str(libro[2]))
    conn.close()
crearTabla()
insertar([('Don Quijote', 'Miguel de Cervantes'), ('1984', 'George Orwell'), ('El Principito', 'Antoine de Saint-Exupéry'), ('Cien años de soledad', 'Gabriel García Márquez'), ('Libro Eliminado', 'Harper Lee')])
borrarLibro()
librosActuales()

# Ejercicio 4
def conexion():
    conn = sqlite3.connect('tienda.db')
    return conn
def crearTabla():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (id INTEGER PRIMARY KEY, producto TEXT, cantidad INTEGER)''')
    conn.commit()
    conn.close()
def insertar(datos):
    conn = conexion()
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO ventas (producto, cantidad) VALUES (?, ?)''', datos)
    conn.commit()
    conn.close()
def borrarProducto():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM ventas WHERE cantidad < 5 ''')
    conn.commit()
    conn.close()
def ventasActuales():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM ventas''')
    ventas = cursor.fetchall()
    for venta in ventas:
        print(venta[1] + " " + str(venta[2]))
    conn.close()
crearTabla()
insertar([('Chocolate', 5), ('Leche', 3), ('Arroz', 7), ('Alfajor', 2), ('Turron', 10)])
borrarProducto()
ventasActuales()