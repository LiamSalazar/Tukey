import matplotlib.pyplot as plt
import random

matriz = [[[0,255,255],[255,0,0],[255,0,0]],
          [[255,0,0],[0,255,255],[255,0,0]],
          [[255,0,0],[255,0,0],[0,255,255]]]

matrizRandom = []
for i in range(3):
    fila = []
    for j in range(3):
        pixel = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        fila.append(pixel)
    matrizRandom.append(fila)

#for i in range(3):
#    fila = []
#    for j in range(3):
#        pixel = []
#        for k in range(3):
#            pixel.append(random.randint(0,255))
#        fila.append(pixel)
#    matrizRandom.append(fila)
print(matrizRandom)

plt.imshow(matrizRandom, cmap="gray")
plt.show()