list = ["a","b","c","d","e"]
list2 = [1,2,3,4,5,6,7,8,9,10]

def range(inicio,fin):
    if inicio < fin:
        print(inicio, end=' ')
        range(inicio+1,fin)
    else:
        print(" ")

def recorrerLista(list, index):
    if index < len(list):
        print(list[index], end=' ')
        recorrerLista(list, index + 1)
    else:
        print(" ")

def miBreak(lista, detener, index):
    if index < len(lista):
        if lista[index] == detener:
            return
        else:
            print(lista[index], end=' ')
            miBreak(lista, detener, index + 1)
    else:
        print(" ")

range(1,11)
recorrerLista(list, 0)
miBreak(list, "c", 0)