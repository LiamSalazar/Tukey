import matplotlib.pyplot as plt

def calcularPromedio(numeros):
    suma = 0
    for i in range(len(numeros)):
        suma += numeros[i]
    return suma / len(numeros)

def calcularVarianza(numeros):
    promedio = calcularPromedio(numeros)
    suma = 0
    for numero in numeros:
        resultado = (numero-promedio)**2
        suma += resultado
    return (suma/len(numeros))

def calcularDesviacionEstandar(numeros):
    return (calcularVarianza(numeros))**(1/2)

nums1 = [2,4,6,8,10,12,14,16,18,20,
        22,1,25,5,7,9,11,13,15,17]
nums2 = [5.1,5.8,6.4,6.0,8.0,7.5,9.1,8.7,9.4,9.5,
        7.4,8.5,7.9,6.0,6.6,7.5,7.9,8.5,8.8,9.2]

#promedio = calcularPromedio(nums)
#varianza = calcularVarianza(nums)
#desviacionEstandar = calcularDesviacionEstandar(nums)

#print(round(promedio, 2))
#print(round(varianza, 2))
#print(round(desviacionEstandar, 2))

plt.scatter(nums1, nums2)
plt.xlabel("Temperatura")
plt.ylabel("Ventas")
plt.title("Ventas a partir de temperatura")
plt.axhline(calcularPromedio(nums2), color = "red")
plt.axvline(calcularPromedio(nums1), color="blue")
plt.show()