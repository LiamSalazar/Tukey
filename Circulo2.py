import matplotlib.pyplot as plt
import math
import random

cantidad = int(input("Cuantos circulos? "))
blanco = [255, 255, 255]
matriz = []
n = 1000
for i in range(n):
    fila = []
    for j in range(n):
        pixel = [0,0,0]
        fila.append(pixel)
    matriz.append(fila)

for i in range(cantidad):
    radio = random.randint(30, 300)
    centroX = random.randint(radio, n-radio-1)
    centroY = random.randint(radio, n-radio-1)

    # y = sqrt(r**2 - (x - centroX)**2) + centroY
    # x = sqrt(r**2 - (y - centroY)**2) + centroX

    for x in range(centroX - radio, centroX + radio + 1):
        diferenciaX = x - centroX
        interiorRaiz = radio**2 - diferenciaX**2
        if interiorRaiz >= 0:
            raiz = math.sqrt(interiorRaiz)
            y1 = int(centroY + raiz)
            y2 = int(centroY - raiz)
            if 0 <= x < n:
                if 0 <= y1 < n:
                    matriz[y1][x] = blanco
                if 0 <= y2 < n:
                    matriz[y2][x] = blanco

    for y in range(centroY - radio, centroY + radio + 1):
        diferenciaY = y - centroY
        interiorRaiz = radio**2 - diferenciaY**2
        if interiorRaiz >= 0:
            raiz = math.sqrt(interiorRaiz)
            x1 = int(centroX + raiz)
            x2 = int(centroX - raiz)
            if 0 <= y < n:
                if 0 <= x1 < n:
                    matriz[y][x1] = blanco
                if 0 <= x2 < n:
                    matriz[y][x2] = blanco

plt.imshow(matriz)
plt.show()
