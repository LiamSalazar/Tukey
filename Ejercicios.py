# Ejercicio 1

cadena = "Abdejdniou"
cadena = cadena.lower()
def esVocal(letra):
    return letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'
def recorrerLista(list,index):
    if index < len(list):
        if esVocal(list[index]):
            print(list[index], end=' ')
        recorrerLista(list, index + 1)
    else:
        print(" ")

recorrerLista(cadena, 0)

# Ejercicio 2
def cuentaRegresiva(inicio, fin):
    if inicio <= fin:
        print(fin, end = ' ')
        if fin == 0:
            print("DESPEGUE")
        cuentaRegresiva(inicio, fin-1)
    else:
        print(" ")

def cuenta(lista, index):
    if index < -(len(lista) + 1):
        print(lista[index], end = ' ')
        cuenta(lista, index - 1)
    else:
        print(" ")

nums = [1,2,3,4,5]

cuenta(nums, -1)

cuentaRegresiva(0,10)