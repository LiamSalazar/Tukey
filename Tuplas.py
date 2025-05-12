import copy

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

#l1 = [1,2,3]
#l2 = [4,5,6]
#l3 = l1
#l4 = l1[:]
#print(id(l1) == id(l3))
#l1.append(10)
#print(l3)
#l1.clear()
#print(l1)
#print(l3)
#print(l4)
#l1.extend(l2)
#l1.remove(2)
#l1.clear()

lista = [1,2,3,4,5]
elimina = [2,3]
def eliminaElementos(lista, elimina):
    n = len(lista)
    i = 0
    while i < n:
        if lista[i] in elimina:
            lista.pop(i)
            n -= 1
        else: i += 1
    return lista
lista = eliminaElementos(lista, elimina)
print("ELIMINADOS")
print(lista)
lita2 = copy.deepcopy(lista)