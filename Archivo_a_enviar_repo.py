def calcular_promedio(lista:list, valor:int)->bool: # lista y valor son los parametros formales
    flag = True
    promedio = 0
    contador = 0
    suma = 0
    for i in range(len(lista)):
        contador += 1
        suma = lista[i]
    promedio = suma / contador
    if promedio > valor:
        flag = False
    return flag
lista =[10,20,30,40]
valor = 80
if calcular_promedio(lista,valor): #INVOCACION de la funcion. Estos son los parametros actuales
    print("el valor es mayor al promedio")
else:
    print("el valor es menor al promedio")
