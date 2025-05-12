numero_1=float(input("Primer numero:"))
operacion=input("Suma:+\nResta:-\nMultiplicacion:*\nDivision:/\nPotencia:**\n\"Tu operacion\": ")
numero_2=float(input("Segundo numero: "))
if operacion[0] == "+":
    print("Tu resultado es: "+str(numero_1+numero_2))
if operacion[0] == "*":
    print("Tu resultado es: "+str(numero_1*numero_2))    
if operacion[0] == "/":
    print("Tu resultado es: "+str(numero_1/numero_2))
if operacion[0] == "-":
    print("Tu resultado es: "+str(numero_1-numero_2))
if operacion[0] == "**":
    print("Tu resultado es: "+str(numero_1**numero_2))

# mas=0
# menos=0
# ecuacion=input("Poner la ecuacion: ")
# posicion_final=ecuacion[-1]
# while ecuacion[mas]!="+" and ecuacion[mas]==ecuacion[-1]:
#     mas+=1
#     if ecuacion[mas] == "+":
#         print(float(ecuacion[:mas])+float(ecuacion[mas:]))
