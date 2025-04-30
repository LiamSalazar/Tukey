def promedio(numeros):
    suma = 0
    for i in range(len(numeros)):
        suma += numeros[i]
    return suma / len(numeros)

def varianza(numeros, promedio):
    suma = 0
    for numero in numeros:
        resultado = ((numero-promedio)**2)
        suma += resultado
    return (suma/len(numeros))

def desviacionEstandar(numeros, promedio):
    return varianza(numeros, promedio)**0.5

def covarianza(x, y):
    suma = 0
    promedioX = promedio(x)
    promedioY = promedio(y)
    for i in range(len(x)):
        suma += (x[i]-promedioX)*(y[i]-promedioY)
    return suma / len(x)

numeros = [1,2,3,4,5]
numeros2 = [2,4,6,8,10]
media = promedio(numeros)
varia = varianza(numeros, media)
desviacion = desviacionEstandar(numeros, media)
covaria = covarianza(numeros, numeros2)
print("El promedio es: ", media)
print("La varianza es: ", varia)
print("La covarianza es: ", covaria)