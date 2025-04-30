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

def covarianza(datos_a, datos_b):
    suma = 0
    for i in range(len(datos_a)):
        suma += (datos_a[i]-calcularPromedio(datos_a))*(datos_b[i]-calcularPromedio(datos_b))
    return suma/len(datos_a)

def correlacion(x,y):
    return covarianza(x,y)/(calcularDesviacionEstandar(x)*calcularDesviacionEstandar(y))

def pendiente(x:list,y:list):
    prom_x = calcularPromedio(x)
    prom_y = calcularPromedio(y)
    n = len(x)
    suma_cuadrados = 0
    suma_productos = 0
    for i in x:
        suma_cuadrados += i**2
    for i in range(len(x)):
        suma_productos += x[i]*y[i]
    m = (suma_productos - n*prom_x*prom_y)/(suma_cuadrados-n*(prom_x)**2)
    return m

def ordenada_origen(x:list, y:list):
    b = calcularPromedio(y) - pendiente(x,y)*calcularPromedio(x)
    return b

# Datos de prueba
horas = [2,4,6,8,10,12,14,16,18,20,
        5,7,9,11,13,15,17]
promedios = [5.1,5.8,6.4,6.0,8.0,7.5,9.1,8.7,9.4,9.5,
            6.0,6.6,7.5,7.9,8.5,8.8,9.2]

# Crear una recta ejemplo
y_modelo = []
for i in range(len(horas)):
    y = (1/4)*horas[i] + 4.5
    y_modelo.append(y)

# Crear recta real
m = pendiente(horas, promedios)
b = ordenada_origen(horas, promedios)
def estimaciones(x:list, y:list):
    y_estimado = []
    for i in range(len(x)):
        Y = pendiente(x,y)*x[i] + ordenada_origen(x,y)
        y_estimado.append(Y)
    return y_estimado

estimados = estimaciones(horas, promedios)

print("M: ", m)
print("B: ", b)
print(correlacion(horas, promedios))
print(calcularDesviacionEstandar(horas))
print(calcularDesviacionEstandar(promedios))

# Graficación de los datos
plt.scatter(horas, promedios) # Datos en ejes (x,y)
plt.xlabel("Horas") # Título en Y
plt.ylabel("Promedios") # Título en X
plt.title("Promedio según horas de estudio") # Título general
#plt.plot(horas, y_modelo) # Graficar recta ejemplo
plt.plot(horas, estimados) # Graficar recta de regresion
plt.show() # Mostrar gráfica

# -1 = Linea de regresion perfecta de pendiente negativa
# 0 = Datos totalmente dispersos, no aplica regresión lineal
# 1 = Datos de regresion perfecta de pendiente positiva
# distancia (Error) = Y real - Y estimado
# Sumatoria de error al cuadrado, aumenta los errores para enfocarse en ellos y no en los
# pequeños, a esto se le llama error cuadrático.
# b = promedio(y)-m*promedio(x)
# m = (Suma(x*y)-n*promedio(x)*promedio(y))/(Suma(x**2)-nx**2)