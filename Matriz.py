nombres = ("Cesar","Santiago","Leni","Leo","Pancho")
edades = (18,18,19,19,17)
carreras = ("CD","CD","CD","IA","SC")

maximo = -1000

for estudiante, edad, carrera in zip(nombres, edades, carreras):
    print(f"Nombre: {estudiante}, Edad: {edad}, Carrera: {carrera}")
    if edad > maximo:
        maximo = edad
        dato = (estudiante, edad, carrera)

print(f"El estudiante de mayor edad es {dato[0]}, tiene {dato[1]} y estudia {dato[2]}")