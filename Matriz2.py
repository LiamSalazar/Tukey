matriz = [[2,3],[4,5]]
print("--------------------")
print("MATRIZ")
print(matriz)
print("--------------------")
print("LISTA")
print(matriz[0])
print("--------------------")
print("VARIABLE")
print(matriz[0][0])
print("--------------------")
print("Impresion matriz al cuadrado")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = matriz[i][j] ** 2
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j])