import math

mensajes_error = [
        "Por favor, introduce un número válido:\n",
        "Inténtalo de nuevo, eso no es un número:\n",
        "Intentos fallidos apilando errores... Intenta de nuevo:\n",
        "Error, acumulacion de intentos fallidos generan problemas en la calculadora...:\n"
    ]

def mostrar_mensaje_error(counter):
    if counter < len(mensajes_error):
        print(mensajes_error[counter])
    else:
        print("Demasiados intentos fallidos. Sistemas fallando. Apagando funciones vitales...\n")
    return counter + 1

def realizar_operacion(numero, numero2, operacion):
    match operacion:
        case "1":
            return int(numero) + int(numero2)
        case "2":
            return int(numero) - int(numero2)
        case "3":
            return int(numero) * int(numero2)
        case "4":
            if int(numero2) != 0:
                return int(numero) / int(numero2)
            else:
                print("Acaso queres destruir el mundo al dividir por 0? Intenta de nuevo.")
                return None
        case "5":
            return int(numero) ** int(numero2)
        case "6":
            return math.sqrt(int(numero))
        case "7":
            return int(numero) ** (1/3)
        case "8":
            print("Adios, que tengas un buen dia")
            exit()
        case _:
            print("Por favor, elige una operacion valida")
            return None

def main():
    counter = 0
    salir = False
    while not salir:
        numero = input("Bienvenido a la calculadora interactiva\nPuedes poner el primer numero para operar:\n")
        if not numero.isdigit():
            counter = mostrar_mensaje_error(counter)
            if counter > len(mensajes_error):
                salir = True
                break
            continue

        while True:
            numero2 = input("Ahora elige el segundo numero para operar:\n")
            if not numero2.isdigit():
                counter = mostrar_mensaje_error(counter)
                if counter > len(mensajes_error):
                    salir = True
                    break
                continue

            operacion = input("Ahora puedes elegir la operacion que quieres realizar\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Potencia\n6. Raiz cuadrada del primer numero\n7. Raiz cubica del primer numero\n8. Salir\nEscribe el numero que corresponda a la operacion que quieres realizar:\n")
            resultado = realizar_operacion(numero, numero2, operacion)
            if resultado is not None:
                print(f"Resultado: {resultado}")
                numero = str(resultado)
                continuar = input("¿Quieres realizar otra operación con el resultado? (s/n):\n")
                if continuar.lower() != 's':
                    print("Gracias por utilizar la calculadora interactiva. Que tenga un buen dia.")
                    salir = True
                    break


main()