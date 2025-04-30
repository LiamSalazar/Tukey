palabra = input("Ingresa una palabra: ")
n = len(palabra)
if n >= 10:
    inicio = palabra[0]
    fin = palabra[n-1]
    cantidad = n-2
    print(inicio,cantidad,fin)
else:
    print(palabra)