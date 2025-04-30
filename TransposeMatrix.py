def transponerMatriz(matriz):
    transpuesta = []
    suma = 0
    for i in range(len(matriz)):
        aux = []
        for j in range(len(matriz[0])):
            if i == j:
                suma += matriz[i][j]
            aux.append(matriz[j][i])
        transpuesta.append(aux)
    return  suma, transpuesta

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
suma, transpuesta = transponerMatriz(matriz)
print("Suma: ", suma)
print("Transpuesta: ", transpuesta)
