x = 1
y = 2
print("VALORES SIN INTERCAMBIAR:")
print("X: ", x)
print("Y: ", y)
y, x = (x,y)
print("VALORES INTERCAMBIADOS:")
print("X: ", x)
print("Y: ", y)

def media(*notacion):
    sum = 0
    for i in notacion:
        sum += i
    return sum / len(notacion)

def funcion(num1, num2):
    division = num1 / num2
    modulo = num1 % num2
    return division, modulo

def cuadrado(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]**2
    return lista

print(media(1,2,3,4,5,6))
print(funcion(10, 5))
print(cuadrado([1,2,3,4,5]))