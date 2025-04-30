import random

secreto = random.randint(1,10)
intentos = 5
while intentos != 0:
    num = int(input("Ingrese su suposición (Número del 1 al 10): "))
    if secreto == num:
        print("Adivinaste")
        break
    elif num > secreto:
        print("Incorrecto")
        print("Es un numero menor")
    elif num < secreto:
        print("Incorrecto")
        print("Es un numero mayor")
    intentos -= 1

print("El numero era: ", secreto)