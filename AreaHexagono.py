l = int(input("Ingrese la medida de un lado del hexágono: "))
perimetro = 6*l
apotema = float((3/4*(l*l))**(1/2))
area = round((perimetro*apotema)/2, 3)
print(f"El area es: {area}")