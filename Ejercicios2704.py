calificaciones_barra1 = [7,5,9,7,9,10,7,7,10,6,7]
calificaciones_barra2 = [10,8,10,7,10,10,7,7,10,6,7]

def calcularPromedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def calcularDesviacionEstandar(lista):
    promedio = calcularPromedio(lista)
    suma = 0
    for numero in lista:
        suma += (numero - promedio) ** 2
    return (suma / len(lista)) ** (1/2)

promedioBarra1 = round(calcularPromedio(calificaciones_barra1), 3)
promedioBarra2 = round(calcularPromedio(calificaciones_barra2), 3)

desviacionEstandarBarra1 = round(calcularDesviacionEstandar(calificaciones_barra1), 3)
desviacionEstandarBarra2 = round(calcularDesviacionEstandar(calificaciones_barra2), 3)

maximaBarra1 = max(calificaciones_barra1)
maximaBarra2 = max(calificaciones_barra2)

minimaBarra1 = min(calificaciones_barra1)
minimaBarra2 = min(calificaciones_barra2)

print("BARRA 1:")
print(f"Promedio: {promedioBarra1} Máxima: {maximaBarra1} Mínima: {minimaBarra1} Desviación estándar: {desviacionEstandarBarra1}\n")

print("BARRA 2:")
print(f"Promedio: {promedioBarra2} Máxima: {maximaBarra2} Mínima: {minimaBarra2} Desviación estándar: {desviacionEstandarBarra2}\n")

# La mejor barra es la 2 porque tiene un promedio más alto y una desviación estándar igual que la de la segunda barra (1.553).

