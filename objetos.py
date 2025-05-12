# Ejercicio 1
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def detalles_coche(self):
        print(f"{self.marca} {self.modelo} {self.año}.")

coche1 = Coche("Toyota", "Corolla", 2020)
coche1.detalles_coche()


# Ejercicio 2
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def es_mas_largo(self, otro_libro):
        if self.paginas > otro_libro.paginas:
            return f"{self.titulo} es más largo que {otro_libro.titulo}."
        else:
            return f"{self.titulo} es más corto que {otro_libro.titulo}."
    
libro1 = Libro("1984", "George Orwell", 328)
libro2 = Libro("Platero y Yo", "Juan Ramón Jiménez", 142)

print(libro1.es_mas_largo(libro2))


# Ejercicio 3
class CuentaBancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self.saldo}")

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")

cuenta1 = CuentaBancaria("Juan Pérez", 1000, "1234567890")
cuenta1.depositar(500)
cuenta1.retirar(200)