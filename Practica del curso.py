sumatorio=0
numero=20
for sumatorio in range(numero):
    sumatorio+=1
    if sumatorio%5==0 or sumatorio%7==0:
        continue
    print(sumatorio)